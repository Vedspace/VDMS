# location/admin.py

from django.contrib import admin
from .models import UserLocation

@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ['user', 'latitude', 'longitude', 'timestamp']
