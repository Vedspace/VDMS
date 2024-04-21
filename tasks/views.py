from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrAssignedUser
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Task


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def mark_task_as_complete(request, task_id):
    try:
        task = Task.objects.get(pk=task_id, assigned_to=request.user)
    except Task.DoesNotExist:
        return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the task is already completed
    if task.completed:
        return Response({'detail': 'Task is already completed.'}, status=status.HTTP_400_BAD_REQUEST)

    task.completed = True
    task.save()
    return Response({'detail': 'Task marked as complete.'})

class TokenLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        token_key = request.data.get("token")
        try:
            token = Token.objects.get(key=token_key)
            # Optionally, return user info or assigned tasks here
            return Response({"success": "Token is valid", "user_id": token.user_id})
        except Token.DoesNotExist:
            return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class UserAssignedTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view returns a list of all tasks for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(assigned_to=user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrAssignedUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        if task.assigned_to != request.user:
            return Response({'message': 'You cannot complete a task not assigned to you.'}, status=status.HTTP_403_FORBIDDEN)

        task.completed = True
        task.completed_by = request.user
        task.save()
        return Response({'status': 'task marked as complete'})
# Django view to fetch tasks marked as done
class CompletedTasksView(APIView):
    def get(self, request):
        # Filter tasks where 'task_done' is True
        tasks = Task.objects.filter(task_done=True).order_by('-completion_date')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
