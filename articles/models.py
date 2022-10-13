from django.db import models

# Create your models here.

class Article(models.Model): # 상속
    title = models.CharField(max_length=10)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


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