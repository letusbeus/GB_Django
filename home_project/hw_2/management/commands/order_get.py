from django.core.management.base import BaseCommand
from hw_2.models import Order


class Command(BaseCommand):
    help = "Get order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        if order:
            self.stdout.write(f'{order}')
        else:
            self.stdout.write(f'No orders were found with the listed ID.')
