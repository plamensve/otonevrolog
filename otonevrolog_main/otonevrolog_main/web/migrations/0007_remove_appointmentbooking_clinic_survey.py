# Generated by Django 5.1.2 on 2024-12-08 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_appointmentbooking_clinic_survey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentbooking',
            name='clinic_survey',
        ),
    ]
