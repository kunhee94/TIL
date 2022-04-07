from multiprocessing import context
from django.shortcuts import render,redirect

import articles
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
        if request.method == 'POST':              
            form = ArticleForm(request.POST)       
            if form.is_valid():                    
                form.save()                       
                return redirect('articles:index') 
    else:
        forms = ArticleForm()
    context = {
        'forms':forms,
    }
    return render(request, 'articles/create.html', context)



