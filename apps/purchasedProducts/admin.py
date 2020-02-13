from django.contrib import admin
from .models import PurchasedProducts


@admin.register(PurchasedProducts)
class PurchasedProductsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Shopping', {
            "fields": (
                ('purchase_type', 'product'), ('price', 'quantity')
            ),
        }),
    )

    list_display = ('product', 'purchase_type', 'quantity', 'price')
    search_fields = ('product', 'purchase_type')
    ordering = ('price', 'product', 'quantity')
    list_filter = ['purchase_type', 'created_at']
