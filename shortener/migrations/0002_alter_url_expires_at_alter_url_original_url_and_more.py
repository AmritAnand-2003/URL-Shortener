# Generated by Django 5.1.4 on 2024-12-07 07:22

import shortener.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='expires_at',
            field=models.DateTimeField(blank=True, default=shortener.models.default_expiry),
        ),
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]