# Generated by Django 3.0.3 on 2020-09-11 18:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rfq', '0011_auto_20200912_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfq',
            name='listing_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
