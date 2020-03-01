from django.contrib import admin
from .models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Manage Inventory', {
            "fields": (
                ('product', 'amount'),
            ),
        }),
    )

    list_display = ('id', 'fullname_product', 'amount',
                    'total_price', 'status_invetory')
    search_fields = ('product__name', 'product__reference__name', 'product__color__name')
    ordering = ('id', 'amount',)
    list_filter = ['created_at']

    def status_invetory(self, obj):
        if obj.amount == 0:
            return 'WARNING'
        elif obj.amount <= 20:
            return 'VERY LOW'
        elif obj.amount <= 40:
            return 'LOW'
        elif obj.amount <= 60:
            return 'GOOD'
        else:
            return 'VERY GOOD'

    def total_price(self, obj):
        price = f'R$ {obj.get_total()}'
        return price

    def fullname_product(self, obj):
        return f"{obj.product.name} {obj.product.reference} {obj.product.color}"

    fullname_product.short_description = 'name'
    total_price.short_description = 'total'
    status_invetory.short_description = 'status'
