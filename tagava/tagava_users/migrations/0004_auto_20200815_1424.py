# Generated by Django 3.1 on 2020-08-15 14:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tagava_users', '0003_auto_20200815_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileotp',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 14, 29, 35, 779141, tzinfo=utc)),
        ),
    ]
