from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = 'Get product with price exact <price>'

    def add_arguments(self, parser):
        parser.add_argument('price', type=float, help='Product price')

    def handle(self, *args, **kwargs):
        price = kwargs['price']
        products = Product.objects.filter(price__exact=price)
        result = '\n'.join(f'{i + 1}. {product}' for i, product in enumerate(products))
        if result:
            self.stdout.write(f'{result}')
        else:
            self.stdout.write(f'No products were found with the listed price {price}.')
