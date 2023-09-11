from django.core.management.base import BaseCommand
from random import choice
# from seminars_project.s2_heads_or_tails.models import GameModel
from s2_heads_or_tails.models import GameModel


class Command(BaseCommand):
    help = 'Play game Head and Tails.'

    def handle(self, *args, **kwargs):
        result = choice(['Heads', 'Tails'])
        game = GameModel(result=result)
        game.save()

        self.stdout.write(f'{game}')
