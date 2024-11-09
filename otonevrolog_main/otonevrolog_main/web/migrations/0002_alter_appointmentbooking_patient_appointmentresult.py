# Generated by Django 5.0.4 on 2024-11-09 14:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentbooking',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AppointmentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nystagmus', models.TextField(max_length=300)),
                ('static_samples', models.TextField(max_length=300)),
                ('kinetic_samples', models.TextField(max_length=300)),
                ('coordination_test', models.TextField(max_length=300)),
                ('fine_coordination', models.TextField(max_length=300)),
                ('other', models.TextField(max_length=300)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment_result', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
