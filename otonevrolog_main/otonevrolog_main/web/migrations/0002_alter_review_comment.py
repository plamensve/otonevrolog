# Generated by Django 5.1.2 on 2024-11-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, default='', max_length=300, null=True),
        ),
    ]