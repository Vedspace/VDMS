from django.db import models
from django.utils import timezone
from django.conf import settings
from .utils import send_push_notification

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_categories'
    )

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100, default="Default Task Name")
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=6, choices=[
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ], default='LOW')
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    completed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='completed_tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    task_done = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        related_name='tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if the task is being created or updated
        if not self.pk:  # New task
            super(Task, self).save(*args, **kwargs)
            if self.assigned_to:
                self.assigned_to.task_assigned_counter += 1
                self.assigned_to.save()
        else:  # Updating task
            old_task = Task.objects.get(pk=self.pk)
            if self.completed and not old_task.completed:
                if self.assigned_to:
                    self.assigned_to.task_done_counter += 1
                    self.assigned_to.save()
            if old_task.assigned_to != self.assigned_to:
                if old_task.assigned_to:
                    old_task.assigned_to.task_assigned_counter -= 1
                    old_task.assigned_to.save()
                if self.assigned_to:
                    self.assigned_to.task_assigned_counter += 1
                    self.assigned_to.save()
            super(Task, self).save(*args, **kwargs)

        if self.pk:
            old_assigned_to = Task.objects.get(pk=self.pk).assigned_to
        else:
            old_assigned_to = None

        super(Task, self).save(*args, **kwargs)

        if self.assigned_to and self.assigned_to != old_assigned_to:
            send_push_notification(
                self.assigned_to,
                "New Task Assigned",
                f"You have been assigned a new task: '{self.name}' with a deadline of {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}."
            )
