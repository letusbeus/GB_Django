from datetime import datetime

from django.core.management.base import BaseCommand
from hw_2.models import Order


class Command(BaseCommand):
    help = 'Get orders for a specific date'

    def add_arguments(self, parser):
        parser.add_argument('placed', type=str, help='Product date (YYYY-MM-DD)')

    def handle(self, *args, **kwargs):
        placed = kwargs['placed']
        try:
            datetime.strptime(placed, '%Y-%m-%d')
        except ValueError:
            self.stdout.write('Invalid date format.')
            return
        orders = Order.objects.filter(placed__exact=placed)
        result = '\n'.join(f'{i + 1}. {order}' for i, order in enumerate(orders))

        self.stdout.write(f'{result}') if result else self.stdout.write(
            f'No orders were found for the listed date: {placed}.')
