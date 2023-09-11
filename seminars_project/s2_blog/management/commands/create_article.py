from random import choice, randint

from django.core.management.base import BaseCommand
from s2_blog.models import Article, Author


class Command(BaseCommand):
    help = 'Create article.'

    def handle(self, *args, **kwargs):
        i = Article.objects.count() + 1
        article = Article(
            title=f'Title{i}',
            content=f'Content{i}',
            date=f'{i}',
            author=choice(Author.objects.all()),
            category=choice(['science', 'religion', 'art', 'politic', 'hobby']),
            views=randint(1, 9999),
            published=choice([False, True])
        )
        article.save()
