# Generated by Django 5.1.2 on 2024-12-08 17:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_clinicsurvey_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicsurvey',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
