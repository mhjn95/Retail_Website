# Generated by Django 3.0.3 on 2020-09-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0041_auto_20200922_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrfqdetails',
            name='complaint',
            field=models.TextField(blank=True, null=True),
        ),
    ]