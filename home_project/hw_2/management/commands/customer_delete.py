from django.core.management.base import BaseCommand
from hw_2.models import Customer


class Command(BaseCommand):
    help = 'Delete Client by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.get(pk=pk)
        if customer is not None:
            customer.delete()
            self.stdout.write(f'Customer ID {pk} has been successfully deleted!')
        else:
            self.stdout.write(f'No customers were found with the listed ID {pk}.')
