from django.shortcuts import render

from .models import ArticlePost


def article_list(request):
    articles = ArticlePost.objects.all()
    # 需要传递给模板的上下文
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    context = {'article': article}
    return render(request, 'article/detail.html', context)
