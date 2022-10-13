from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('dinner/<str:name>/', views.dinner),
    path('review/', views.review, name='review'),
    path('review/result/', views.review, name='review_result'),
]