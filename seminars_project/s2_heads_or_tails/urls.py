from django.urls import path
from . import views

app_name = 's2_heads_or_tails'

urlpatterns = [
    path('play_game/', views.play_game, name='play_game'),
    path('last_games/', views.last_games, name='last_games'),
]