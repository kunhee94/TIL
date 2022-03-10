from unicodedata import name
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('edit/<int:article_id>/', views.edit, name='edit'),
    path('update/<int:article_id>/', views.update, name='update'),
    path('delete/<article_id>/', views.delete, name='delete'),
]
