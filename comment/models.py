from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey



class Comment(MPTTModel):
    article = models.ForeignKey(
        ArticlePost,on_delete=models.CASCADE,related_name='comments'
    )
    user = models.ForeignKey(
        User,on_delete=models.CASCADE,related_name='comments'
    )
    body = RichTextField()
    created=models.DateTimeField(auto_now=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    reply_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replyers'
    )

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.body[:20]
