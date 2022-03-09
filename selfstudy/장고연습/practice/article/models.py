from django.db import models

# Create your models here.

class animall(models.Model):
    name = models.CharField(max_length=4)
    find = models.CharField(max_length=3)
    age = models.IntegerField()


    def __str__(self):
        return f'{self.name}, {self.age}'
