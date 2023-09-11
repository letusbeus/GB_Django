from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('dice_master/', views.dice_master, name='dice_master'),
    path('randomizer/', views.randomizer, name='randomizer'),
]
