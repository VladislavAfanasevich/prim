# Generated by Django 2.1.5 on 2019-02-07 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='comments',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Редактирование'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='Комментарий'),
        ),
    ]
