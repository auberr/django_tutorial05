from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'name': name,
    }
    return render(request, 'dinner.html', context)
