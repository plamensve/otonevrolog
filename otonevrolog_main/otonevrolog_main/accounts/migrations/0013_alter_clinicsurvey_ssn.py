# Generated by Django 5.1.2 on 2024-12-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_clinicsurvey_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicsurvey',
            name='ssn',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True),
        ),
    ]
