# Generated by Django 2.0.2 on 2018-07-06 12:32

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0015_auto_20180705_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudquestionnaire',
            name='alteration_risk',
            field=models.BooleanField(default=False, help_text='No person or organisation will be harmed if the information is altered by mistake or intentionally by a wrongdoer.', verbose_name='Information Alteration'),
        ),
        migrations.AlterField(
            model_name='cloudquestionnaire',
            name='continuity_risk',
            field=models.BooleanField(default=False, help_text='We will be able to carry on our activities if the service is disrupted or is unavailable for an extended.', verbose_name='Business Continuity'),
        ),
        migrations.AlterField(
            model_name='cloudquestionnaire',
            name='disclosure_risk',
            field=models.BooleanField(default=False, help_text='The information is publicly available or it can be de-identified so that its release into the public domain would not compromise our obligations to a person or an organisation.', verbose_name='Privacy Breach'),
        ),
        migrations.AlterField(
            model_name='cloudquestionnaire',
            name='loss_risk',
            field=models.BooleanField(default=False, help_text='No person or orginastion will be harmed if the information is lost by the cloud provider OR we can easily maintain a local copy of the information.', verbose_name='Data Loss'),
        ),
        migrations.AlterField(
            model_name='ictvendorassessment',
            name='host_country',
            field=django_countries.fields.CountryField(help_text='1. What country or countries is the service hosted in?', max_length=2),
        ),
    ]
