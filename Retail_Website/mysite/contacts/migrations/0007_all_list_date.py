# Generated by Django 3.0.3 on 2020-09-04 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_all'),
    ]

    operations = [
        migrations.AddField(
            model_name='all',
            name='list_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
