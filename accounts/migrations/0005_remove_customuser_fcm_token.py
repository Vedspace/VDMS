# Generated by Django 5.0 on 2024-04-14 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_fcm_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fcm_token',
        ),
    ]
