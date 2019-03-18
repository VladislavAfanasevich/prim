# Generated by Django 2.1.5 on 2019-03-17 16:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_auto_20190317_1920'),
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
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 17, 16, 34, 0, 400934, tzinfo=utc)),
        ),
    ]