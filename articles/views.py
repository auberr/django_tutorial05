from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from articles.models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request):
    menus = [{'name':'족발', 'price':30000}, {'name':'햄버거', 'price':5000}, {'name':'치킨', 'price':20000}, {'name':'초밥', 'price':40000}]
    pick = random.choice(menus)
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk') #pk의 역순으로 배치
    context = {
        'pick': pick,
        'menus': menus,
        'articles': articles,
    }
    return render(request, 'dinner.html', context)

def review(request):
    if request.method == 'GET':
        return render(request, 'review.html')
    elif request.method == 'POST':
        content = request.POST.get('content')
        title = request.POST.get('title')
        article = Article(title=title, content=content)
        article.save()

        return redirect('articles:detail', article.pk)

        # return redirect('/articles/dinner/temporal/') # 임시 하드코딩

        # print(request.POST)
        # context = {
        #     'content' : content,
        # }
        # return render(request, 'review_result.html', context) #삭제


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    
    if request.method == 'POST':    
        article.delete()

    return redirect('articles:dinner')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'edit.html', context)
    
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)