from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from PIL import Image

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
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    tags = TaggableManager(blank=True)
    avatar = models.ImageField(upload_to='article/%Y%m%d/',blank=True)
    def save(self, *args, **kwargs):
        article = super(ArticlePost, self).save(*args, **kwargs)

        if self.avatar and not kwargs.get('update_fileds'):
            image=Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y=int(new_x*(y/x))
            resized_image=image.resize((new_x,new_y),Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article


    # 用于给model定义元数据
    class Meta:
        # 数据以创建时间的倒序排列
        ordering = ('-created',)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article:detail',args=[self.id])

