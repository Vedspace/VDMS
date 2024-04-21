from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import DeviceToken
from rest_framework import status

from .serializers import DeviceTokenSerializer

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        password = request.data.get('password')
        device_token = request.data.get('device_token')

        user = authenticate(username=phone, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            if device_token:
                DeviceToken.objects.update_or_create(
                    user=user,
                    defaults={'token': device_token}
                )
            return Response({
                "token": token.key,
                "message": "Login successful and device token updated"
            })
        else:
            return Response({"error": "Invalid Credentials"}, status=400)
class StoreDeviceTokenView(APIView):
    def post(self, request):
        serializer = DeviceTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)