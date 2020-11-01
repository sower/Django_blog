from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


# 博客文章数据模型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    # 用于给model定义元数据
    class Meta:
        # 数据以创建时间的倒序排列
        ordering = ('-created',)

    def __str__(self):
        return self.title
