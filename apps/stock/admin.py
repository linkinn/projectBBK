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

    list_display = ('fullname_product', 'amount',
                    'total_price', 'status_invetory')
    search_fields = ('product', 'product__reference', 'product__color')
    ordering = ('amount',)
    list_filter = ['created_at']

    def status_invetory(self, obj):
        if obj.amount < 10:
            return 'low'
        return 'high'

    def total_price(self, obj):
        price = f'R$ {obj.get_total()}'
        return price

    def fullname_product(self, obj):
        return f"{obj.product.name} {obj.product.reference} {obj.product.color}"

    fullname_product.short_description = 'name'
    total_price.short_description = 'total'
    status_invetory.short_description = 'status'
