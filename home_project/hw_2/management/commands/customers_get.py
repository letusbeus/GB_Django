from django.core.management.base import BaseCommand
from hw_2.models import Customer


class Command(BaseCommand):
    help = "Get all customers."

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        result = '\n'.join(f'{i + 1}. {customer}' for i, customer in enumerate(customers))
        if result:
            self.stdout.write(f'{result}')
        else:
            self.stdout.write(f'No customers were found.')
