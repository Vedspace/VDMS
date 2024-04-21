from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('heading', 'content')
    search_fields = ('heading', 'content')
    list_filter = ('heading',)

admin.site.register(Notification, NotificationAdmin)
