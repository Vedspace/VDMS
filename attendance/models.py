from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Attendance(models.Model):
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time1 = models.DateTimeField(null=True, blank=True, default=now)
    time2 = models.DateTimeField(null=True, blank=True, default=now)
    time3 = models.DateTimeField(null=True, blank=True, default=now)



    def __str__(self):
        return f"{self.worker.phone} - {self.date}"
