from django.core.management.base import BaseCommand
from .order_create import Command as OrderCreateCommand


class Command(BaseCommand):
    help = 'Create orders.'

    def add_arguments(self, parser):
        parser.add_argument('counter', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        counter = kwargs.get('counter')
        for i in range(counter):
            OrderCreateCommand.handle(self)
