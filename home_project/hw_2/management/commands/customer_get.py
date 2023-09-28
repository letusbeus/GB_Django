from django.core.management.base import BaseCommand
from hw_2.models import Customer


class Command(BaseCommand):
    help = "Get customer by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        customer = Customer.objects.filter(pk=pk).first()
        if customer:
            self.stdout.write(f'{customer}')
        else:
            self.stdout.write(f'No customers were found with the listed ID.')
