# Generated by Django 5.1.4 on 2024-12-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_url_expires_at_alter_url_original_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.BigIntegerField(default=100000000001)),
            ],
        ),
    ]
