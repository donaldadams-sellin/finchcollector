from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25)
    favorite_music = models.CharField(max_length=25)
    age = models.IntegerField()
