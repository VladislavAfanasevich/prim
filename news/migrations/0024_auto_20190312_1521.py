# Generated by Django 2.1.5 on 2019-03-12 12:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20190304_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_of_creation',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 12, 12, 21, 15, 629460, tzinfo=utc)),
        ),
    ]