# Generated by Django 5.1.2 on 2024-11-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(max_length=300),
        ),
    ]