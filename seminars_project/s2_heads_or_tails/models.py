from django.db import models
from django.db.models import Manager, Model


class GameModel(Model):
    """
    Создайте модель для запоминания бросков монеты: орёл или решка.
    Также запоминайте время броска.
    Добавьте статический метод для статистики по n последним броскам монеты.
    Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
    """
    result = models.CharField(max_length=10)
    played = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'Result: {self.result}, played at: {self.played}'

    @staticmethod
    def last_games(n):
        return GameModel.objects.all().order_by('-played')[:n]
