from django.contrib import admin
from django.utils import timezone
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'format_time1', 'format_time2', 'format_time3')

    def make_aware(self, datetime_obj):
        if timezone.is_naive(datetime_obj):
            return timezone.make_aware(datetime_obj, timezone.get_default_timezone())
        return datetime_obj

    def format_time1(self, obj):
        local_time = self.make_aware(obj.time1)
        return local_time.strftime('%Y-%m-%d %H:%M:%S') if obj.time1 else None
    format_time1.admin_order_field = 'time1'
    format_time1.short_description = 'Time 1'

    def format_time2(self, obj):
        local_time = self.make_aware(obj.time2)
        return local_time.strftime('%Y-%m-%d %H:%M:%S') if obj.time2 else None
    format_time2.admin_order_field = 'time2'
    format_time2.short_description = 'Time 2'

    def format_time3(self, obj):
        local_time = self.make_aware(obj.time3)
        return local_time.strftime('%Y-%m-%d %H:%M:%S') if obj.time3 else None
    format_time3.admin_order_field = 'time3'
    format_time3.short_description = 'Time 3'

admin.site.register(Attendance, AttendanceAdmin)
