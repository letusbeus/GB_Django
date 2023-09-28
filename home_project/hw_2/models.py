from django.db import models
from django.db.models import Manager, Model


class Customer(Model):
    objects = Manager()

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    address = models.TextField(max_length=200)
    registered = models.DateField()

    @property
    def get_name(self):
        return f'{self.name}'
    
    def __str__(self):
        return (
            f'ID: {self.id}, '
            f'customer: {self.name}, '
            f'email: {self.email}, '
            f'phone number: {self.phone}, '
            f'address: {self.address}, '
            f'registration date: {self.registered}'
        )


class Product(Model):
    objects = Manager()

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()
    added = models.DateField()
    product_img = models.ImageField(default=0)

    @property
    def get_title(self):
        return f'{self.title}'

    def __str__(self):
        return (
            f'ID: {self.id}, '
            f'product: {self.title}, '
            f'description: {self.description}, '
            f'price: {self.price}, '
            f'quantity: {self.quantity}, '
            f'added: {self.added}'
        )


class Order(Model):
    objects = Manager()

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    placed = models.DateField()

    def __str__(self):
        return (
            f'Order ID: {self.id}, '
            f'customer: {self.customer.name}, '
            f'total price: {self.total}, '
            f'placed: {self.placed}'
        )
