# Generated by Django 4.0.9 on 2023-02-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_availability_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='enable_reminders',
            field=models.BooleanField(default=False),
        ),
    ]
