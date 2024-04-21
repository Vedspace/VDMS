from django.urls import path
from .views import LoginAPIView,StoreDeviceTokenView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('store-device-token/', StoreDeviceTokenView.as_view(), name='store_device_token'),
]

