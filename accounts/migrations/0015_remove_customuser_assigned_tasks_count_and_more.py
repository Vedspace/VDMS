# Generated by Django 5.0 on 2024-04-14 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_customuser_assigned_tasks_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='assigned_tasks_count',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='completed_tasks_count',
        ),
    ]