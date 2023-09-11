from django.core.management.base import BaseCommand
from s2_blog.models import Article, Author


class Command(BaseCommand):
    help = 'Get all articles.'

    def handle(self, *args, **kwargs):
        articles = list(Article.objects.all())

        self.stdout.write(f'{articles}')
