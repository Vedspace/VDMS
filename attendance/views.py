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
        # Get or create an attendance record for today
        attendance, created = Attendance.objects.get_or_create(
            worker=request.user,
            date=timezone.now().date(),
            defaults={'time1': timezone.now().time()}
        )
        
        # If already created, update the next time slot
        if not created:
            if not attendance.time2:
                attendance.time2 = timezone.now().time()
            elif not attendance.time3:
                attendance.time3 = timezone.now().time()
            attendance.save()
        
        return Response({
            "status": "success",
            "data": AttendanceSerializer(attendance).data
        }, status=status.HTTP_200_OK)

# Adjust the permission_classes as per your project’s security requirements
