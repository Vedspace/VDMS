# Generated by Django 5.0 on 2024-04-14 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='points',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='tasks_assigned',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='tasks_completed',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
