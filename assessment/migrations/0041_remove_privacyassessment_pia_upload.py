# Generated by Django 2.0.2 on 2018-07-11 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0040_privacyassessment_disclaimer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privacyassessment',
            name='pia_upload',
        ),
    ]
