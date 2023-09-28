from django.core.management.base import BaseCommand
from .product_create import Command as ProductCreateCommand


class Command(BaseCommand):
    help = 'Create fake products.'

    def add_arguments(self, parser):
        parser.add_argument('counter', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        counter = kwargs.get('counter')
        for i in range(counter):
            ProductCreateCommand.handle(self)
