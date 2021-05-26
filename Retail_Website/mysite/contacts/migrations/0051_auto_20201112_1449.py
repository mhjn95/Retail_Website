# Generated by Django 3.0.3 on 2020-11-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0050_quotesrecieved_resolution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotesrecieved',
            old_name='resolution',
            new_name='resolutions',
        ),
        migrations.AddField(
            model_name='quotesrecieved',
            name='resolutionmade',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]