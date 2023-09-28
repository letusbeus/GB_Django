from django.core.management.base import BaseCommand
from hw_2.models import Customer


class Command(BaseCommand):
    help = 'Update customer by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client Name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        customer = Customer.objects.filter(pk=pk).first()
        if customer is not None:
            customer.name = name
            customer.save()
            self.stdout.write(f'Customer:"{customer}" has been successfully updated!')
        else:
            self.stdout.write(f'No customers were found with the listed ID {pk}.')
