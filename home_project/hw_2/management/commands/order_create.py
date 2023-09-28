import random
from django.core.management.base import BaseCommand
from hw_2.management.commands.my_command import generate_random_date
from hw_2.models import Order, Customer, Product
from .customers_create import Command as CustomersCreateCommand
from .products_create import Command as ProductsCreateCommand


class Command(BaseCommand):
    help = 'Create order.'

    def handle(self, *args, **kwargs):
        if not Customer.objects.all():
            CustomersCreateCommand.handle(self, counter=3)
        if not Product.objects.all():
            ProductsCreateCommand.handle(self, counter=10)
        order = Order(
            customer=random.choice(Customer.objects.all()),
            total=0.00,
            placed=generate_random_date(2022, 2022))
        order.save()
        select_goods = [random.choice(Product.objects.all()) for _ in range(5)]
        order.product.set(select_goods)
        order.total = sum(good.price for good in select_goods)
        order.save()
        self.stdout.write(f'New order has been created:\n{order}')
