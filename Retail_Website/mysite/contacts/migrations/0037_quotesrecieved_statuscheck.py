# Generated by Django 3.0.3 on 2020-09-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0036_auto_20200919_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotesrecieved',
            name='statuscheck',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
