from django import forms
from .models import ArticlePost


# 文章表单
class ArticlePostForm(forms.ModelForm):

    class Meta:
        model = ArticlePost
        fields = ('title', 'body', 'tags')
