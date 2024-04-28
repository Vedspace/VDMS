from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Task

@receiver(post_delete, sender=Task)
def update_counters_on_task_deletion(sender, instance, **kwargs):
    if instance.assigned_to:
        instance.assigned_to.task_assigned_counter -= 1
        if instance.completed:
            instance.assigned_to.task_done_counter -= 1
        instance.assigned_to.save()

@receiver(post_save, sender=Task)
def update_counters_on_task_save(sender, instance, created, **kwargs):
    if created:
        if instance.assigned_to:
            instance.assigned_to.task_assigned_counter += 1
            instance.assigned_to.save()
    else:
        old_task = sender.objects.get(pk=instance.pk)
        if instance.completed and not old_task.completed:
            instance.assigned_to.task_done_counter += 1
            instance.assigned_to.save()
        if old_task.assigned_to != instance.assigned_to:
            if old_task.assigned_to:
                old_task.assigned_to.task_assigned_counter -= 1
                if old_task.completed:
                    old_task.assigned_to.task_done_counter -= 1
                old_task.assigned_to.save()
            if instance.assigned_to:
                instance.assigned_to.task_assigned_counter += 1
                if instance.completed:
                    instance.assigned_to.task_done_counter += 1
                instance.assigned_to.save()
