# Generated by Django 2.0.2 on 2018-07-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0046_auto_20180717_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catmeeting',
            name='meeting_code',
            field=models.CharField(default='CAT<built-in method today of type object at 0x0000000051C03340>126', max_length=100, primary_key=True, serialize=False),
        ),
    ]
