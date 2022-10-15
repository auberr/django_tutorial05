from django.db import models
from django.conf import settings
from foods.models import Food

# Create your models here.

class Article(models.Model): # 상속
    title = models.CharField(max_length=10)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default='')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return f'{self.user} {self.content}'

# concept code
'''
class Dog:
    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed='Lab')
grankd = Dog(breed='Huskie')


class Review:
    title = ''
    content = ''
    user= ''

    def __init__(self, content=content, title=title, user=user):
        self.content = content
        self.title = title
        self.user = user

review1 = Review(title="인생 영화", content="어쩌구 저쩌구111", user="권기현")
'''