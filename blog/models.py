from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, )
    publish_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    status_published_post = models.BooleanField(default=False, verbose_name='Статус поста')
    category = models.ForeignKey('Category', verbose_name='Категория', blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/ProectBlog/img/', null=True, blank=True )



    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)




    def __str__(self):
        return f'{self.text}'


class Category(models.Model):
    text = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return f'{self.text}'


