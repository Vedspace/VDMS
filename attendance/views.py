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

        # Get or create an attendance record for today
        attendance, created = Attendance.objects.get_or_create(
            worker=request.user,
            date=timezone.now().date(),
            defaults={time_slot: timezone.now().time()}
        )

        # If the record already exists, and the time slot is not yet marked, update it
        if not created:
            current_time = getattr(attendance, time_slot)
            if current_time is None:
                setattr(attendance, time_slot, timezone.now().time())
                attendance.save()

        return Response({
            "status": "success",
            "data": AttendanceSerializer(attendance).data
        }, status=status.HTTP_200_OK)
