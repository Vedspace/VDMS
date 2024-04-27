from django.contrib import admin
from django.utils import timezone
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'format_time1', 'format_time2', 'format_time3')

    def format_time1(self, obj):
        return self.localize_time(obj.time1)
    format_time1.admin_order_field = 'time1'  # Allows column order sorting
    format_time1.short_description = 'Time 1'  # Column header

    def format_time2(self, obj):
        return self.localize_time(obj.time2)
    format_time2.admin_order_field = 'time2'
    format_time2.short_description = 'Time 2'

    def format_time3(self, obj):
        return self.localize_time(obj.time3)
    format_time3.admin_order_field = 'time3'
    format_time3.short_description = 'Time 3'

    def localize_time(self, datetime_obj):
        """Converts naive datetime to timezone-aware datetime for display."""
        if datetime_obj is None:
            return None
        if timezone.is_naive(datetime_obj):
            # Assume datetime is in UTC, make it timezone aware and convert to local timezone
            datetime_obj = timezone.make_aware(datetime_obj, timezone.utc)
        return timezone.localtime(datetime_obj).strftime('%Y-%m-%d %H:%M:%S')
