from django.http import HttpResponse
from random import choice, randint
import logging

logger = logging.getLogger(__name__)


# def index(request):
#     return HttpResponse('Hello, World!')


def heads_or_tails(request):
    result = choice(['Heads', 'Tails'])
    logger.info(f"'Heads or Tails' page accessed, {result = }")
    return HttpResponse(result)


def dice_master(request):
    result = randint(1, 6)
    logger.info(f"'Dice master page accessed' page accessed, {result = }")
    return HttpResponse(result)


def randomizer(request):
    result = randint(1, 100)
    logger.info(f"'Randomizer page accessed' page accessed, {result = }")
    return HttpResponse(result)
