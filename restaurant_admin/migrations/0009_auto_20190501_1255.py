# Generated by Django 2.1.7 on 2019-05-01 08:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0008_auto_20190430_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 8, 25, 50, 532853, tzinfo=utc)),
        ),
    ]