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
        time_slot = request.data.get('time_slot')
        valid_slots = ['time1', 'time2', 'time3']

        if time_slot not in valid_slots:
            return Response({'error': 'Invalid time slot specified'}, status=status.HTTP_400_BAD_REQUEST)

        # Get or create an attendance record for today using the local time
        today = timezone.localtime().date()  # Ensuring the date is as per Asia/Kolkata timezone
        current_time = timezone.localtime().time()  # The current time in Asia/Kolkata timezone

        attendance, created = Attendance.objects.get_or_create(
            worker=request.user,
            date=today,
            defaults={time_slot: current_time}
        )

        # If already created, update the next time slot only if it's not set
        if not created:
            current_time_slot = getattr(attendance, time_slot)
            if current_time_slot is None:
                setattr(attendance, time_slot, current_time)
                attendance.save()

        return Response({
            "status": "success",
            "data": AttendanceSerializer(attendance).data
        }, status=status.HTTP_200_OK)
