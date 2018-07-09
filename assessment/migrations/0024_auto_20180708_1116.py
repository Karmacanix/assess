# Generated by Django 2.0.2 on 2018-07-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0023_applicationtype_icon_html'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalapplication',
            name='application_type',
        ),
        migrations.AddField(
            model_name='application',
            name='dhbs',
            field=models.ManyToManyField(to='assessment.DHBs'),
        ),
        migrations.RemoveField(
            model_name='application',
            name='application_type',
        ),
        migrations.AddField(
            model_name='application',
            name='application_type',
            field=models.ManyToManyField(to='assessment.ApplicationType', verbose_name='Type'),
        ),
    ]
