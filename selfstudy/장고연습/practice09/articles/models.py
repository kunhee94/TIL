from cgitb import text
from django.db import models
from accounts.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField()
    author_id = models.ForeignKey(User, models.CASCADE)