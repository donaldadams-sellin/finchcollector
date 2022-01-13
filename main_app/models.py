from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)

    def __str__(self):
        return f'Toy {self.id} - {self.name}'
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'toy_id': self.id})


class Finch(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25)
    favorite_music = models.CharField(max_length=25)
    age = models.IntegerField()
    toys = ManyToManyField(Toy)

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
    TIMES = (
    ('D', 'Day'),
    ('N', 'Night')
    )
    FOODS = (
        ('S', 'Seeds'),
        ('I', 'Insect')
    )
    date = models.DateField()
    time = models.CharField(max_length=1, choices=TIMES, default=TIMES[0][0])
    food = models.CharField(max_length=1, choices=FOODS, default=FOODS[0][0])
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'Fed {self.get_food_display()} at {self.get_time_display()} on {self.date}'

    class Meta:
        ordering = ['-date']
