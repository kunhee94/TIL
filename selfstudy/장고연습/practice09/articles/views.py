from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author_id = request.user
            todo.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/new.html', context)