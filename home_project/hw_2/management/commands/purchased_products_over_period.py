from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from hw_2.models import Order, Product


class Command(BaseCommand):
    help = 'Get products from a specific customer\'s orders for a specified period.'

    def add_arguments(self, parser):
        parser.add_argument('customer_id', type=int, help='Customer ID')
        parser.add_argument('period', type=int, help='Number of days for the period')

    def handle(self, *args, **kwargs):
        customer_id = kwargs['customer_id']
        period = kwargs['period']
        end_date = datetime.now()
        start_date = end_date - timedelta(days=period)

        orders = Order.objects.filter(customer__id=customer_id, placed__range=(start_date, end_date)).order_by(
            '-placed')

        if orders.exists():
            products = Product.objects.filter(order__in=orders).distinct()
            result = '\n'.join(f'{i + 1}. {product}' for i, product in enumerate(products))
            self.stdout.write(f'Products purchased by the customer ID {customer_id} over the last {period} days:\n{result}')
        else:
            self.stdout.write(f'Customer ID {customer_id} has not placed any orders for the last {period} days.')
