from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ProductAddForm
from .management.commands.my_command import generate_random_date
from .models import Customer, Product, Order
from .management.commands.customer_create import Command as CustomerCommand
from .management.commands.product_create import Command as ProductCommand
from .management.commands.order_create import Command as OrderCommand

import logging

logger = logging.getLogger(__name__)


def customer_products_get(request, customer_id, period):
    customer_id = int(customer_id)
    period = int(period)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=period)

    orders = Order.objects.filter(customer__id=customer_id, placed__range=(start_date, end_date)).order_by(
        '-placed')

    if orders.exists():
        products = Product.objects.filter(order__in=orders).distinct()
        return render(request, 'hw_2/customer_products.html', {
            'customer_id': customer_id,
            'period': period,
            'products': products,
        })
    else:
        return render(request, 'hw_2/customer_products.html', {
            'customer_id': customer_id,
            'period': period,
            'products': [],
        })


def customer_create(request):
    logger.info('Customer creation has been requested.')
    create_customer_command = CustomerCommand()
    create_customer_command.handle()
    latest_customer = Customer.objects.latest('id')
    result = (f'New customer has been registered:<br>'
              f'Name: {latest_customer.name},<br>'
              f'Email: {latest_customer.email},<br>'
              f'Phone: {latest_customer.phone},<br>'
              f'Address: {latest_customer.address},<br>'
              f'Registration date: {latest_customer.registered}')
    return HttpResponse(result)


def customers_get(request):
    logger.info('Customers list has been requested.')
    result = '<br>'.join(str(i) for i in Customer.objects.all())
    return HttpResponse(result)


def customer_get(request):
    pass


def product_create(request):
    logger.info('Product creation has been requested.')
    create_product_command = ProductCommand()
    create_product_command.handle()
    latest_product = Product.objects.latest('id')
    result = (f'New product has been successfully added:<br>'
              f'{latest_product.title},<br>'
              f'{latest_product.description},<br>'
              f'{latest_product.price},<br>'
              f'{latest_product.quantity},<br>'
              f'{latest_product.added}')
    return HttpResponse(result)


def product_img_create(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        message = 'New product been successfully added!'
        if form.is_valid():
            product_title = form.cleaned_data['product_title']
            product_description = form.cleaned_data['product_description']
            product_price = form.cleaned_data['product_price']
            product_quantity = form.cleaned_data['product_quantity']
            product_image = form.cleaned_data['product_image']
            # fs = FileSystemStorage()
            # fs.save(product_image.name, product_image)
            logger.info(
                f'New product been successfully added: \n{product_title}, {product_description}, {product_price}, {product_quantity}, '
                f'{product_image.name}.')
            product = Product(title=product_title, description=product_description,
                              price=product_price, quantity=product_quantity,
                              product_img=product_image, added=generate_random_date(2021, 2023))
            product.save()
    else:
        form = ProductAddForm()
        message = 'Please submit the form: '
    return render(request, 'hw_2/product_img_create.html', {'form': form, 'message': message})


def products_create(request):
    pass


def products_get(request):
    result = '<br>'.join(str(i) for i in Product.objects.all())
    return HttpResponse(result)


def product_get(request):
    pass


def order_create(request):
    create_order_command = OrderCommand()
    create_order_command.handle()
    latest_order = Order.objects.latest('id')
    result = (f'New order has been placed:<br>'
              f'{latest_order}')
    return HttpResponse(result)


def orders_get(request):
    result = '<br>'.join(str(i) for i in Order.objects.all())
    return HttpResponse(result)


def order_get(request):
    pass


def customer_min_orders(request):
    pass


def customer_max_orders(request):
    pass


def product_price_gt(request):
    pass


def product_price_lt(request):
    pass


def product_price_exact(request):
    pass


def orders_from_user(request):
    pass


def orders_for_date(request):
    pass
