from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

class AttendanceViewSet(viewsets.ModelViewSet):
    # existing setup...

    @action(detail=False, methods=['post'])
    def mark_attendance(self, request):
        time_slot = request.data.get('time_slot')
        valid_time_slots = ['time1', 'time2', 'time3']
        if time_slot not in valid_time_slots:
            return Response({"error": "Invalid time slot"}, status=status.HTTP_400_BAD_REQUEST)

        attendance, created = Attendance.objects.get_or_create(
            worker=request.user,
            date=timezone.now().date(),
            defaults={time_slot: timezone.now().time()}
        )

        if not created and getattr(attendance, time_slot) is None:
            setattr(attendance, time_slot, timezone.now().time())
            attendance.save()

        return Response({
            "status": "success",
            "data": AttendanceSerializer(attendance).data
        }, status=status.HTTP_200_OK)
