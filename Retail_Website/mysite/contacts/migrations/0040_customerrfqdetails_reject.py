# Generated by Django 3.0.3 on 2020-09-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0039_auto_20200922_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrfqdetails',
            name='reject',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]