from django.contrib import admin
from .models import DeviceToken

class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'created_at']  # Columns to display in the admin list view
    search_fields = ['user__username', 'token']  # Fields to search in the admin list view
    list_filter = ['created_at']  # Filters available in the sidebar
    raw_id_fields = ['user']  # Makes the user field a search field to easily find users

admin.site.register(DeviceToken, DeviceTokenAdmin)
