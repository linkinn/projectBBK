from django.contrib import admin
from .models import PurchasedProducts


@admin.register(PurchasedProducts)
class PurchasedProductsAdmin(admin.ModelAdmin):
    list_display = ('purchased_provider',
                    'purchase_type', 'quantity', 'price')
    search_fields = ('purchased_provider__name', 'purchased_provider__note_number')
    ordering = ('purchased_provider__purchase_date', 'price', 'quantity')
    list_filter = ['purchased_provider__purchase_date', 'created_at']
