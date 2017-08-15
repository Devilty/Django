from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'MyModel/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'MyModel/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'MyModel/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'MyModel/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    category = request.POST.get('category', 'Category')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content, category=category)
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.category = category
        article.save()
    # articles = models.Article.objects.all()
    # return render(request, 'MyModel/index.html', {'articles': articles})
    # articles = models.Article.objects.all()
    return HttpResponseRedirect('/blog/index')
