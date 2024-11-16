# Generated by Django 5.1.2 on 2024-11-09 18:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_appointmentbooking_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentbooking',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]