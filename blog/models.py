from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, )
    publish_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    status_published_post = models.BooleanField(default=False, verbose_name='Статус поста')


    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)


    def __str__(self):
        return f'{self.text}'
