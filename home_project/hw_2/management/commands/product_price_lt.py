from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = 'Get product with price less then <price>'

    def add_arguments(self, parser):
        parser.add_argument('price', type=float, help='Product price')

    def handle(self, *args, **kwargs):
        price = kwargs['price']
        products = Product.objects.filter(price__lt=price)
        result = '\n'.join(f'{i + 1}. {product}' for i, product in enumerate(products))
        if result:
            self.stdout.write(f'{result}')
        else:
            self.stdout.write(f'No products were found with a price lower than {price}.')
