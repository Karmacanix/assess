# Generated by Django 2.0.2 on 2018-07-10 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0034_auto_20180711_0251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catmeeting',
            name='meeting_time_date',
        ),
        migrations.AddField(
            model_name='catmeeting',
            name='meeting_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date:'),
        ),
    ]