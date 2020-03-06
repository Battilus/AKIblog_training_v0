from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    views = models.IntegerField(default=0)
    #photos
    #videos

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