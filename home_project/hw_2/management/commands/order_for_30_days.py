from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from hw_2.models import Order, Product


class Command(BaseCommand):
    help = 'Get products from a specific customer\'s orders for the last 30 days.'

    def add_arguments(self, parser):
        parser.add_argument('customer', type=str, help='Customer ID')

    def handle(self, *args, **kwargs):
        customer = kwargs['customer']
        month_ago = datetime.now() - timedelta(days=30)
        orders = Order.objects.filter(customer=customer, placed__gte=month_ago).order_by('-placed')

        if orders.exists():
            products = Product.objects.filter(order__in=orders).distinct()
            result = '\n'.join(f'{i + 1}. {product}' for i, product in enumerate(products))
            self.stdout.write(result)
        else:
            self.stdout.write(f'Customer ID {customer} has not placed any orders in the last 30 days.')
