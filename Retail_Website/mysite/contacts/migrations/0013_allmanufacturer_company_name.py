# Generated by Django 3.0.3 on 2020-09-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_contactmanufacturer_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmanufacturer',
            name='company_name',
            field=models.TextField(null=True),
        ),
    ]