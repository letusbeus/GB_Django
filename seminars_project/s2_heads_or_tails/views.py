from random import choice
from django.http import HttpResponse
from .models import GameModel


def play_game(request):
    result = choice(['Heads', 'Tails'])

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')


def last_games(request):
    last_game = GameModel.last_games(3)
    result = '<br>'.join(str(i) for i in last_game)

    return HttpResponse(result)
