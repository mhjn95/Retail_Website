# Generated by Django 3.0.3 on 2020-09-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfq', '0006_rfq_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfq',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]