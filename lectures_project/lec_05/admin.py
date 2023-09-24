from django.contrib import admin
from .models import Category, Product


@admin.action(description='Set quantity to zero ')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Products list"""
    list_display = ('name', 'category', 'quantity')
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description', 'name']
    search_help_text = 'Search by description field'
    actions = [reset_quantity]

    """Product"""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']  # displaying fields
    readonly_fields = ['date_added', 'rating']  # set readonly fields
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
