from django.urls import path
from .views import TaskCountersView, UserProfileView
# urls.py






urlpatterns = [
    # your other urls
    path('task-counters/', TaskCountersView.as_view(), name='task-counters'),
     path('api/user-profile/', UserProfileView.as_view(), name='user-profile'),
]
