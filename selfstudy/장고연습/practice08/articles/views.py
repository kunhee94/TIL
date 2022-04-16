from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ArticleForm,CommentForm
from .models import Article,Comment
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
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
    }
    return render(request,'articles/create.html',context)


def detail(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    form = CommentForm()
    comments = article.comment_set.all()

    # orm으로 구하기
    total =  comments.count()
    blue = comments.filter(pick='blue').count()
    red = total-blue

    #for문으로 구하기
    # blue_cnt, red_cnt = 0,0
    # for comment in comments:
    #     if comment.pick == 'blue':
    #         blue_cnt += 1
    #     else:
    #         red_cnt += 1

    context = {
        'article':article,
        'form':form,
        'comments':comments,
        'red_per': red / total * 100 if total else 0,
        'blue_per': blue / total * 100 if total else 0,
        
    }
    return render(request, 'articles/detail.html', context)


def comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail', article.pk)


