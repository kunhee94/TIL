from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
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
        'form': form,
        'title':'CREATE',
        'send_btn':'글 작성',
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form':form,
        'title':'UPDATE',
        'send_btn':'글 수정',
        'article': article
    }
    return render(request, 'articles/form.html', context)

def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method =='POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article_pk)
