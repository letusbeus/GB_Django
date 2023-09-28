from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = 'Update product title by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('title', type=str, help='Product title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        title = kwargs.get('title')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.title = title
            product.save()
            self.stdout.write(f'Product {product} has been successfully updated!')
        else:
            self.stdout.write(f'No products were found with the listed ID {pk}.')
