# Generated by Django 3.0.3 on 2020-09-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfq', '0004_auto_20200902_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfq',
            name='process',
            field=models.TextField(blank=True, null=True),
        ),
    ]
