from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class Category(models.Model):
    title = models.CharField('Категория', max_length=50)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Tag(models.Model):

    title = models.CharField('Тэг', max_length=50)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title


class News(models.Model):
    # класс новостей

    user = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=150)
    text_description = models.TextField('Описание текста', max_length=300)
    text = models.TextField('Текст ')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    date_of_creation = models.DateTimeField(timezone.now())

    # Для поисковых систем
    keywords = models.CharField('Ключевые слова', max_length=50)
    description = models.CharField('Описание', max_length=100)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date_of_creation']

    def __str__(self):
        return self.title


class Comments(models.Model):
    # Комментарии к новостям

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE)
    new = models.ForeignKey(
        News,
        verbose_name='Новость',
        on_delete=models.CASCADE)
    text = models.TextField('Комментарий', max_length=300)
    date = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    moderation = models.BooleanField('Редактирование', default=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)


