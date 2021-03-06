# Generated by Django 2.1.5 on 2019-04-30 05:12

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0006_auto_20190430_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='phone_number',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34|56|13|77|76|61|38|58|35|84)\\d{7}$')]),
        ),
        migrations.AlterField(
            model_name='worker',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 30, 5, 12, 17, 31306, tzinfo=utc)),
        ),
    ]
