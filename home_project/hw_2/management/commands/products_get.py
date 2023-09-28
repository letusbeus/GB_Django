from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        result = '\n'.join(f'{i + 1}. {product}' for i, product in enumerate(products))
        if result:
            self.stdout.write(f'{result}')
        else:
            self.stdout.write(f'No products were found.')
