# Generated by Django 3.0.3 on 2020-11-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0052_quotesrecieved_complaintitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotesrecieved',
            name='complaintchoices',
            field=models.TextField(blank=True, null=True),
        ),
    ]
