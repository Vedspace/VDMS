# Generated by Django 5.0 on 2024-04-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
