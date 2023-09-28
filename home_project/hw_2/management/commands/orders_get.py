from django.core.management.base import BaseCommand
from hw_2.models import Order


class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        result = '\n'.join(f'{i + 1}. {order}' for i, order in enumerate(orders))
        if result:
            self.stdout.write(f'{result}')
        else:
            self.stdout.write(f'No orders were found.')
