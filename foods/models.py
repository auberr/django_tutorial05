from email.policy import default
from django.db import models

# Create your models here.

class Genre(models.Model):
    class Meta:
        db_table = "genre"
    name = models.CharField(max_length=70, default='')


class Food(models.Model):
    class Meta:
        db_table = "food"
    name = models.CharField(max_length=70, default='')
    original_title = models.CharField(max_length=70, default='')
    genre = models.ManyToManyField(Genre, related_name='foods')
    shop = models.CharField(max_length=70, default='')
    rated = models.CharField(max_length=70, default='')
    launched_date = models.CharField(max_length=70, default='')
    desc = models.TextField(max_length=256, default='')
    img = models.TextField(max_length=256, default='')
