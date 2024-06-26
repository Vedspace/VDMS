from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Attendance
from .serializers import AttendanceSerializer
from django.conf import settings

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def mark_attendance(self, request):
        time_slot = request.data.get('time_slot', 'time1')  # Default to 'time1' if not specified
        valid_time_slots = ['time1', 'time2', 'time3']

        # Ensure the provided time slot is valid
        if time_slot not in valid_time_slots:
            return Response({'error': 'Invalid time slot'}, status=status.HTTP_400_BAD_REQUEST)

        local_now = timezone.localtime(timezone.now())  # Convert to local timezone

        # Get or create an attendance record for today using the local date
        attendance, created = Attendance.objects.get_or_create(
            worker=request.user,
            date=local_now.date(),  # Use local date
            defaults={time_slot: local_now.time()}  # Use local time for the default time slot
        )

        # If the record already exists, and the time slot is not yet marked, update it
        if not created:
            current_time = getattr(attendance, time_slot)
            if current_time is None:
                setattr(attendance, time_slot, local_now.time())  # Set with local time
                attendance.save()

        return Response({
            "status": "success",
            "data": AttendanceSerializer(attendance).data
        }, status=status.HTTP_200_OK)
