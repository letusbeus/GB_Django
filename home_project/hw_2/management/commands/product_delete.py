from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = 'Delete Product by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        if product is not None:
            product.delete()
            self.stdout.write(f'Product ID {pk} has been successfully deleted!')
        else:
            self.stdout.write(f'No products were found with the listed ID {pk}.')
