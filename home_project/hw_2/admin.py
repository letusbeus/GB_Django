from django.contrib import admin
from .models import Customer, Product, Order


@admin.action(description='Set quantity to zero')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Products list"""
    list_display = ('title', 'price', 'quantity')
    ordering = ['title', '-quantity']
    list_filter = ['added', 'price', 'quantity']
    search_fields = ['description', 'title']
    search_help_text = 'Search by description & title fields'
    actions = [reset_quantity]

    """Product"""
    readonly_fields = ['added']  # set readonly fields
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Specification',
                'fields': ['description'],
            },
        ),
        (
            'Accounting',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'More',
            {
                'description': 'Product added date',
                'fields': ['product_img', 'added'],
            }
        ),
    ]


class CustomerAdmin(admin.ModelAdmin):
    """Customers list"""
    list_display = ('name', 'phone', 'email', 'registered')
    ordering = ['name', 'registered']
    list_filter = ['registered', 'name']
    search_fields = ['name', 'phone', 'email']
    search_help_text = 'Search by name, email & phone fields'
    # actions = [reset_quantity]

    """Customer"""
    readonly_fields = ['registered']  # set readonly fields
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Contacts',
            {
                'classes': ['collapse'],
                'description': 'Contact info',
                'fields': ['email', 'phone'],
            },
        ),
        (
            'More',
            {
                'description': 'Registration date',
                'fields': ['registered'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    """Orders list"""
    list_display = ('customer', 'total', 'placed')
    ordering = ['placed', '-total']
    list_filter = ['total', 'customer', 'placed']
    search_fields = ['customer', 'total']
    search_help_text = 'Search by customer & total price'

    """Order"""
    readonly_fields = ['placed', 'customer']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Details',
            {
                'classes': ['wide'],
                'description': 'Order details',
                'fields': ['total', 'placed'],
            },
        ),
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
