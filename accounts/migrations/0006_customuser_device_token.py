# Generated by Django 5.0 on 2024-04-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_fcm_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='device_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
