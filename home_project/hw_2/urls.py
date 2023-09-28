from django.urls import path
from . import views

app_name = 'hw_2'


urlpatterns = [
    path('customer_create/', views.customer_create, name='customer_create'),
    path('customers_get/', views.customers_get, name='customers_get'),
    path('customer_get/', views.customer_get, name='customer_get'),
    path('customer_min_orders/', views.customer_min_orders, name='customer_min_orders'),
    path('customer_max_orders/', views.customer_max_orders, name='customer_max_orders'),
    path('product_create/', views.product_create, name='product_create'),
    path('products_create/', views.products_create, name='products_create'),
    path('product_get/', views.product_get, name='product_get'),
    path('products_get/', views.products_get, name='products_get'),
    path('product_price_gt/', views.product_price_gt, name='product_price_gt'),
    path('product_price_lt/', views.product_price_lt, name='product_price_lt'),
    path('product_price_exact/', views.product_price_exact, name='product_price_exact'),
    path('order_create/', views.order_create, name='order_create'),
    path('orders_get/', views.orders_get, name='orders_get'),
    path('order_get/', views.order_get, name='order_get'),
    path('orders_from_user/', views.orders_from_user, name='orders_from_user'),
    path('orders_for_date/', views.orders_for_date, name='orders_for_date'),
    path('customer_products_get/<int:customer_id>/<int:period>/', views.customer_products_get, name='customer_products_get'),
    path('product_img_create/', views.product_img_create, name='product_img_create'),
]
