from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


class ArticleColumn(models.Model):
    '栏目的model'
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



# 博客文章数据模型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    tags=TaggableManager(blank=True)


    # 用于给model定义元数据
    class Meta:
        # 数据以创建时间的倒序排列
        ordering = ('-created',)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article:detail',args=[self.id])

