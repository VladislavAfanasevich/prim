# Generated by Django 2.1.5 on 2019-03-17 16:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0029_auto_20190312_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_of_creation']},
        ),
        migrations.AlterField(
            model_name='comments',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_of_creation',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 17, 16, 20, 30, 537667, tzinfo=utc)),
        ),
    ]
