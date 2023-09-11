from django.db import models
from django.db.models import Manager, Model


class Customer(Model):
    objects = Manager()

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(max_length=11)
    address = models.TextField(max_length=200)
    registered = models.DateField()

    @property
    def get_name(self):
        return f'{self.name}'
    
    def __str__(self):
        return (
            f'Customer: {self.name}, '
            f'email: {self.email}, '
            f'phone number: {self.phone}, '
            f'address: {self.address}, '
            f'registration date: {self.registered}'
        )


class Product(Model):
    objects = Manager()

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField()
    quantity = models.IntegerField()
    added = models.DateField()

    @property
    def get_title(self):
        return f'{self.title}'

    def __str__(self):
        return (
            f'Product: {self.title}, '
            f'description: {self.description}, '
            f'price: {self.price}, '
            f'quantity: {self.quantity}, '
            f'added: {self.added}'
        )


class Order(Model):
    objects = Manager()

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    total = models.DecimalField()
    placed = models.DateField()

    def __str__(self):
        return (
            f'Customer: {self.customer.get_name}, '
            f'product: {self.product.get_title}, '
            f'total price: {self.total}, '
            f'placed: {self.placed}'
        )
