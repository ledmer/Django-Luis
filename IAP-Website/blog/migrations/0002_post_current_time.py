# Generated by Django 4.2.6 on 2023-10-07 09:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='current_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
