# Generated by Django 2.1.5 on 2019-02-13 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20190213_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='Новость'),
        ),
    ]
