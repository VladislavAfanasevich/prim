# Generated by Django 2.1.5 on 2019-02-07 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190207_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='Новость'),
        ),
    ]
