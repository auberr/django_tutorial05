from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from articles.models import Article, Comment
from django.http import HttpResponse
from django.http import JsonResponse
from foods.models import Food

import random

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
    comment = Comment.objects.get(pk=pk)
    context = {
        'article': article,
        'comment': comment
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


@csrf_exempt
def food_article(request, food_pk):
    if request.method =='POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        food = Food.objects.get(pk=food_pk)
        article = Article(title=title, content=content, user=request.user, food=food)
        article.save()
        return JsonResponse({"status":"글 등록 완료"})

@csrf_exempt
def food_like(request, article_pk, food_pk):
    if request.method =='POST':
        article = Article.objects.get(pk=article_pk)
        article.like_users.add(request.user)
        article.save()
        return JsonResponse({"status":"좋아요 완료"})

    if request.method =='GET':
        article = Article.objects.get(pk=article_pk)
        likes = list(article.like_users.all().values('username'))
        return JsonResponse({"like":likes})

@csrf_exempt
def food_comment(request, article_pk, food_pk):
    if request.method == 'POST':
        content = request.POST.get('content', None)
        article = Article.objects.get(pk=article_pk)
        comment = Comment(user=request.user, content=content, article=article)
        comment.save()
        return JsonResponse({"status":"댓글 등록 완료"})

    elif request.method == 'GET':
        article = Article.objects.get(pk=article_pk)
        comments = list(article.comment_set.all().values())

        return JsonResponse({"comments":comments})
