from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from tasks.models import Task
# views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            'phone': user.phone,
            'name': user.name,
            'balance': user.amount,
            'device_token':user.device_token
            # Include other relevant user information here
        }
        return Response(data)

class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.name


class TaskCountersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        tasks_assigned_count = Task.objects.filter(assigned_to=user).count()
        tasks_done_count = Task.objects.filter(completed_by=user).count()

        return Response({
            'tasks_assigned_count': tasks_assigned_count,
            'tasks_done_count': tasks_done_count
        })

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def update_fcm_token(request):
    token = request.data.get('fcm_token')
    if token:
        request.user.fcm_token = token
        request.user.save()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
