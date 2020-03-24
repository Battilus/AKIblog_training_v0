from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone
import datetime


def slugify_fx(content):
    return content.replace('_', '-').lower()

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    # slug = models.SlugField(blank=True, null=True, unique=True)
    slug = AutoSlugField(populate_from='article_title', slugify_function=slugify_fx)
    #photos
    #videos
    #TODO При загрузке фото на лету создавать папку с ID статьи и грузить туда изображения

    def __str__(self):
        return self.article_title

    def was_published_recently(self, in_days=7):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=in_days))

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    article_af = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return ("{}, {}, {}").format(self.author_name, self.comment_text, self.pub_date)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'


#TODO
#likes
#Добавить вывод в список админки имя автора коммента, текст и названии статьи к которой привязан коммент