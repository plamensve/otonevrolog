# Generated by Django 5.1.2 on 2024-10-30 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_appointmentslot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentslot',
            name='date',
        ),
        migrations.AddField(
            model_name='appointmentslot',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.appointmentbooking'),
        ),
    ]
