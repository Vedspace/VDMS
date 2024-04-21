import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Hometasks.routing  # This will contain WebSocket URL routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hometasks.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Hometasks.routing.websocket_urlpatterns
        )
    ),
})
