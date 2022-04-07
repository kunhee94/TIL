from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
        'title':'CREATE',
        
    }
    return render(request, 'articles/create.html', context)


def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)


def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'title':'UPDATE',
        'form':form
    }
    return render(request, 'articles/create.html', context)


def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article_pk)