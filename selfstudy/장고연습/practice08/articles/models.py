from tkinter import CASCADE
from turtle import title
from django.db import models
from django.forms import CharField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    pick = models.CharField(max_length=10)
    content = models.CharField(max_length=100)