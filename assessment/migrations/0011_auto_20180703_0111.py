# Generated by Django 2.0.2 on 2018-07-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0010_auto_20180702_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='assess_status',
            field=models.CharField(choices=[('N', 'New'), ('A', 'Assessing'), ('R', 'Rejected'), ('P', 'Approved')], default='N', max_length=1, verbose_name='Status'),
        ),
    ]
