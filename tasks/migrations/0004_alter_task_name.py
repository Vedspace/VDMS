# Generated by Django 5.0 on 2024-04-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_time_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='Default Task Name', max_length=100),
        ),
    ]
