from django.urls import path
from . import views

app_name = 's2_blog'

urlpatterns = [
    path('get_authors/', views.get_authors, name='get_authors'),
    path('get_articles/', views.get_articles, name='get_articles'),
    path('create_article/', views.create_article, name='create_article'),
]