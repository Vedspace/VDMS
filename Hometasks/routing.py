from django.urls import path
from . import consumers  # This will be your WebSocket consumer

websocket_urlpatterns = [
    path('ws/tasks/', consumers.NotificationConsumer.as_asgi()),
]
