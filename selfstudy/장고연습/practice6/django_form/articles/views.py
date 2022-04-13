from django.shortcuts import render, redirect
from .models import Article,Comment
from .forms import ArticleForm,CommentForm


def index(request):
    # 모든 데이터를 DB에서 가져온다.
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        # 1. 사용자의 입력을 채운 form 인스턴스를 만든다.
        print(request.POST)
        form = ArticleForm(request.POST)
        # 2. 유효성 검사를 한다.
        if form.is_valid():
            # 3. 유효성 검사를 통과하면 저장한다.
            article = form.save()
            # 4. 다음 페이지로 리다이렉트 한다.
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article,
    }

    return render(request, 'articles/form.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()  # DB에서 삭제
        return redirect('articles:index')
    
    return redirect('articles:detail', article.pk)


def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article_pk)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)