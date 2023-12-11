from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=256)
    article = models.ManyToManyField(Article, related_name='tag_name', through='PositionTag')

    def __str__(self):
        return self.tag


class PositionTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tags')
    is_main = models.BooleanField(blank=False)