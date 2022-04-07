from unicodedata import name
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.index, name='index'),
    path('create/', views.create, name='create')
]
