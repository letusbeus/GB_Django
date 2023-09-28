from django.core.management.base import BaseCommand
from hw_2.models import Order


class Command(BaseCommand):
    help = 'Get orders from a specific customer'

    def add_arguments(self, parser):
        parser.add_argument('customer', type=str, help='Customer ID')

    def handle(self, *args, **kwargs):
        customer = kwargs['customer']
        orders = Order.objects.filter(customer__exact=customer)
        result = '\n'.join(f'{i + 1}. {order}' for i, order in enumerate(orders))

        self.stdout.write(f'{result}') if result else self.stdout.write(
            f'No orders were found for the customer ID {customer}.')
