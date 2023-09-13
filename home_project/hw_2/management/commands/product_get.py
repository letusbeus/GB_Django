from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        if product:
            self.stdout.write(f'{product}')
        else:
            self.stdout.write(f'No products were found with the listed ID.')
