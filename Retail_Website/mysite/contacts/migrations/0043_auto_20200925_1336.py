# Generated by Django 3.0.3 on 2020-09-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0042_customerrfqdetails_complaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerrfqdetails',
            name='complaint',
        ),
        migrations.AddField(
            model_name='quotesrecieved',
            name='complaint',
            field=models.TextField(blank=True, null=True),
        ),
    ]
