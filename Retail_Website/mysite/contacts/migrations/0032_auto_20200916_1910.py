# Generated by Django 3.0.3 on 2020-09-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0031_auto_20200916_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotesrecieved',
            name='reject',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
