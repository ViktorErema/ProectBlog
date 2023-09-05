from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    publish_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)


    def __str__(self):
        return f'{self.title}'
