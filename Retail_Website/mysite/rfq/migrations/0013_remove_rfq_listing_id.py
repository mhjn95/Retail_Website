# Generated by Django 3.0.3 on 2020-09-11 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfq', '0012_auto_20200912_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfq',
            name='listing_id',
        ),
    ]
