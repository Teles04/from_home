from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Teg(models.Model):
    teg = models.CharField(max_length=50, verbose_name='Тэг')
    articles = models.ManyToManyField(Article, blank=True, related_name='articles',
                                  through='MainArticleChoice',
                                  )
    def __str__(self):
        return self.teg

class MainArticleChoice(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    teg = models.ForeignKey(Teg, on_delete=models.CASCADE)
    main_article = models.BooleanField()

