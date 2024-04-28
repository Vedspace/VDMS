from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CategoryViewSet, UserAssignedTasksView, TokenLoginView, mark_task_as_complete

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'categories', CategoryViewSet, basename='category')  # Registering the Category viewset

urlpatterns = [
    path('', include(router.urls)),
    path('my-tasks/', UserAssignedTasksView.as_view(), name='my-tasks'),
    path('api/token-login/', TokenLoginView.as_view(), name='token_login'),
    path('api/tasks/<int:task_id>/complete/', mark_task_as_complete, name='mark-task-complete'),
]
