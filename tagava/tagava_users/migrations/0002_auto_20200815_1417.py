# Generated by Django 3.1 on 2020-08-15 14:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tagava_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileotp',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 14, 22, 6, 731841, tzinfo=utc)),
        ),
    ]
