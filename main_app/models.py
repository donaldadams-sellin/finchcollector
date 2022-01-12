from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25)
    favorite_music = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id})