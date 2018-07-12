# Generated by Django 2.0.2 on 2018-07-10 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0030_auto_20180710_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catmeeting',
            name='absentees',
        ),
        migrations.AlterField(
            model_name='catmeeting',
            name='meeting_minutes',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Minutes:'),
        ),
        migrations.AlterField(
            model_name='catmeeting',
            name='meeting_time_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 11, 2, 40, 54, 233223), verbose_name='Date & time:'),
        ),
    ]