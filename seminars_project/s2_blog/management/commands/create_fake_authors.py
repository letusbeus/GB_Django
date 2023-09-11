from random import randint

from django.core.management.base import BaseCommand
from s2_blog.models import Author


class Command(BaseCommand):
    help = 'Create fake authors.'

    def add_arguments(self, parser):
        parser.add_argument('counter', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        counter = kwargs.get('counter')
        for i in range(1, counter + 1):
            author = Author(
                name=f'AuthorName{i}',
                lastname=f'AuthorLastname{i}',
                mail=f'mail{i}@mail.ru',
                bio=f'Biography{i}',
                bdate=f'{randint(1952, 1991)}-{randint(1, 12)}-{randint(1, 31)}'

            )
            author.save()
