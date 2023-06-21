# Create your models here.
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')  # 複数行の入力欄
    # djangoで現在時間を取得するときは『timezone.now』
    # timezone.nowをdefaultにいれると、現在時刻がデフォルトで入力済みになる
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')

    # タグは複数紐づく。また、タグを設定しないことも可能にしている(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='タグ')

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField('名前', default='名無し', max_length=255)
    text = models.TextField('コメント内容')
    target = models.ForeignKey(
        Article, on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='紐づく記事'
    )

    def __str__(self):
        return self.text[:50]
