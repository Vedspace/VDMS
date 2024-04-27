from django.contrib import admin
from django.utils import timezone
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'format_time1', 'format_time2', 'format_time3')

    def format_time1(self, obj):
        return self.format_time(obj.time1)
    format_time1.admin_order_field = 'time1'
    format_time1.short_description = 'Time 1'

    def format_time2(self, obj):
        return self.format_time(obj.time2)
    format_time2.admin_order_field = 'time2'
    format_time2.short_description = 'Time 2'

    def format_time3(self, obj):
        return self.format_time(obj.time3)
    format_time3.admin_order_field = 'time3'
    format_time3.short_description = 'Time 3'

    def format_time(self, datetime_obj):
        """Formats a datetime object to display in the local timezone."""
        if datetime_obj is None:
            return 'Not Marked'  # or any other placeholder you prefer
        if timezone.is_naive(datetime_obj):
            # Assume the datetime is in UTC for making it timezone aware
            datetime_obj = timezone.make_aware(datetime_obj, timezone.utc)
        # Convert to local time in the Asia/Kolkata timezone
        local_datetime = timezone.localtime(datetime_obj, timezone.get_default_timezone())
        return local_datetime.strftime('%Y-%m-%d %H:%M:%S')


admin.site.register(Attendance, AttendanceAdmin)
