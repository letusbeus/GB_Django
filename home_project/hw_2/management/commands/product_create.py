from random import randint
from django.core.management.base import BaseCommand
from .my_command import generate_random_date
from hw_2.models import Product


class Command(BaseCommand):
    help = 'Create product.'

    def handle(self, *args, **kwargs):
        product = Product(
            price=f'{randint(10, 9999) / 100}',
            quantity=f'{randint(0, 99)}',
            added=f'{generate_random_date(2010, 2022)}'
        )
        product.save()
        i = Product.objects.latest('id').id
        product.title = f'Product_{i}'
        product.description = f'Product_description_{i}'
        product.save()
        self.stdout.write(f'New product has been successfully added:\n{product}')
