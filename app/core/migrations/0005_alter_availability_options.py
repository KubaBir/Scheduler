# Generated by Django 4.0.9 on 2023-02-10 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_availability'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'permissions': [('add', 'Post a new lesson'), ('join', 'Join a lesson')]},
        ),
    ]
