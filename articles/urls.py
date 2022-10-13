from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner, name='dinner'),
    path('dinner/review/', views.review, name='review'),
    path('dinner/review/result/', views.review, name='review_result'),
    path('dinner/review/<int:pk>/', views.detail, name='detail'),
    path('dinner/review/<int:pk>/delete/', views.delete, name='delete'),
    path('dinner/review/<int:pk>/edit/', views.edit, name='edit'),
    path('dinner/review/<int:pk>/update/', views.update, name='update'),
]