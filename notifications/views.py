from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from django.contrib.auth import get_user_model
from pyfcm import FCMNotification

User = get_user_model()

class SendNotification(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can send notifications

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            notification = serializer.save()

            # Fetch the user to send the notification to
            try:
                phone = request.data.get('phone')
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)

            if not user.device_token:
                return Response({'error': 'No device token available for the user'}, status=404)

            push_service = FCMNotification(api_key="AAAAC8z0aAU:APA91bHL5sPpu8Rcgj_gMfuMk4A3DaBHzz8tyVJt4byzUiRD7kfRLfV0PiVcXZIPKz-nB4R3ASNfHp28i_A9bVWclrF0oDBOwa_mKpqPeN2fTEijPww1qPKVEKbVNybUDo9UkUw2o1p6")

            # Send notification to the specific device
            result = push_service.notify_single_device(
                registration_id=user.device_token,
                message_title=notification.heading,
                message_body=notification.content,
            )

            return Response({'message': 'Notification sent!', 'result': result})
        return Response(serializer.errors, status=400)
