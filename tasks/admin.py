from django.contrib import admin
from django.utils import timezone
from .models import Task
from datetime import timedelta

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'upload_date', 'assigned_to', 'completed', 'completed_by', 'completion_date', 'deadline_display', 'time_left')
    list_filter = ('completed', 'priority', 'assigned_to', 'completed_by')
    search_fields = ('name', 'description')

    def deadline_display(self, obj):
        return obj.deadline.strftime('%Y-%m-%d %H:%M:%S') if obj.deadline else None

    def time_left(self, obj):
        if obj.deadline:
            now = timezone.now()
            time_left = obj.deadline - now
            return str(time_left) if time_left.total_seconds() > 0 else "Deadline Passed"
        return None

    deadline_display.short_description = "Deadline"
    time_left.short_description = "Time Left"

admin.site.register(Task, TaskAdmin)
