from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404

import articles
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    return render(request, 'articles/create.html')

def new(request):
    article = Article(title=f"{request.POST.get('title')}", content=f"{request.POST.get('content')}")
    article.save()

    return redirect('articles:detail', article.id)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.id)

def delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
    return redirect('articles:index')