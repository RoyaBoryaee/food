# Generated by Django 2.1.7 on 2019-05-31 16:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0011_auto_20190513_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 31, 16, 20, 48, 960514, tzinfo=utc)),
        ),
    ]
