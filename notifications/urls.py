from django.urls import path
from .views import SendNotification

urlpatterns = [
    path('send/', SendNotification.as_view(), name='send-notification'),
]
