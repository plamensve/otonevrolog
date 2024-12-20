# Generated by Django 5.1.2 on 2024-12-11 16:07

import otonevrolog_main.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_appointmentbooking_ssn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentbooking',
            name='ssn',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True, validators=[otonevrolog_main.web.validators.validate_ssn]),
        ),
    ]
