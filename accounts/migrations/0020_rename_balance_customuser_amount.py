# Generated by Django 5.0 on 2024-04-19 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_customuser_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='balance',
            new_name='amount',
        ),
    ]
