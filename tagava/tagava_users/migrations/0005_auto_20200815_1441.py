# Generated by Django 3.1 on 2020-08-15 14:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tagava_users', '0004_auto_20200815_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileotp',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 14, 41, 55, 30311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mobileotp',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 14, 46, 55, 30338, tzinfo=utc)),
        ),
    ]
