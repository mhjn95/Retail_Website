# Generated by Django 3.0.3 on 2020-09-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0037_quotesrecieved_statuscheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrfqdetails',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
