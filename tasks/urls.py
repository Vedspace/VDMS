# Assuming you have this setup already
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import mark_task_as_complete


from .views import TaskViewSet,LoginView,TokenLoginView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    
    path('my-tasks/', views.UserAssignedTasksView.as_view(), name='my-tasks'),
    path('api/token-login/', TokenLoginView.as_view(), name='token_login'),
    path('api/tasks/<int:task_id>/complete/', mark_task_as_complete, name='mark-task-complete'),
]
