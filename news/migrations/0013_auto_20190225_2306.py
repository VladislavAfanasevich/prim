# Generated by Django 2.1.5 on 2019-02-25 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20190219_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='Новость'),
        ),
    ]
