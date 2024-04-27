from django.db import models
from django.conf import settings
from django.utils import timezone

class Attendance(models.Model):
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time1 = models.TimeField(null=True, blank=True)
    time2 = models.TimeField(null=True, blank=True)
    time3 = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.worker.name} - {self.date}"
