from django.shortcuts import render,redirect

from .models import ArticlePost
import markdown
from django.http import HttpResponse
from .forms import ArticlePostForm
from django.contrib.auth.models import User





def article_list(request):
    articles = ArticlePost.objects.all()
    # 需要传递给模板的上下文
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
    extensions=['markdown.extensions.extra',
    'markdown.extensions.codehilite'])

    context = {'article': article}
    return render(request, 'article/detail.html', context)



def article_create(request):
    if request.method == 'POST':
        article_post_form=ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author=User.objects.get(id=1)
            new_article.save()
            return redirect('article:list')
        else:
            return HttpResponse('表单有误，请重新填写')
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html',context)

def article_delete(request, id):
    article=ArticlePost.objects.get(id=id)
    article.delete()
    return redirect('article:list')

def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect('article:list')
    else:
        return HttpResponse('请求错误')