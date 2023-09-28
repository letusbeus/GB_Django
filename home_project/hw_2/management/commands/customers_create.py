from django.core.management.base import BaseCommand
from .customer_create import Command as CustomerCreateCommand


class Command(BaseCommand):
    help = 'Create fake customers.'

    def add_arguments(self, parser):
        parser.add_argument('counter', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        counter = kwargs.get('counter')
        for i in range(counter):
            CustomerCreateCommand.handle(self)
