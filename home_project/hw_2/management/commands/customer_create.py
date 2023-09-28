from random import randint
from django.core.management.base import BaseCommand
from .my_command import generate_random_date
from hw_2.models import Customer


class Command(BaseCommand):
    help = 'Create customer.'

    def handle(self, *args, **kwargs):
        customer = Customer(
            phone=f'8{randint(9000000000, 9999999999)}',
            registered=f'{generate_random_date(2010, 2022)}'
        )
        customer.save()
        i = Customer.objects.latest('id').id
        customer.name = f'Customer{i}'
        customer.email = f'customer{i}@mail.ru'
        customer.address = f'address{i}'
        customer.save()
        self.stdout.write(f'New customer has been successfully registered:\n{customer}')
