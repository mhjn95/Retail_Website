# Generated by Django 3.0.3 on 2020-09-15 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0022_auto_20200913_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotesRecieved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimatecost', models.IntegerField(blank=True, null=True)),
                ('estimatedays', models.IntegerField(blank=True, null=True)),
                ('moreinfo', models.TextField(blank=True, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
