from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField('Категория',max_length=50)
    class Meta():
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
class Tag(models.Model):

    title = models.CharField('Тэг', max_length=50)

    class Meta():
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title



# класс новостей
class News(models.Model):


    user = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True)
    category = models.ForeignKey(Category, verbose_name='Категория',on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=150)
    text_description = models.TextField('Описание текста', max_length=300)
    text = models.TextField('Текст ')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    date_of_creation = models.DateTimeField(auto_now_add=True)

    #Для поисковых систем
    keywords = models.CharField('Ключевые слова', max_length=50)
    description = models.CharField('Описание',max_length=100)

    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
