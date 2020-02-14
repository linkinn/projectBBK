from django.contrib import admin
from apps.purchasedProducts.models import PurchasedProducts
from .models import PurchasedProvider


class PurchasedProductsInline(admin.TabularInline):
    model = PurchasedProducts
    extra = 1


@admin.register(PurchasedProvider)
class PurchasedProviderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Shopping', {
            "fields": (
                ('name', 'note_number'), 'purchase_date', 'total'
            ),
        }),
    )
    readonly_fields = ('total',)
    list_display = ('name', 'note_number', 'purchase_date', 'total')
    search_fields = ('name', 'note_number')
    ordering = ('purchase_date',)
    list_filter = ['purchase_date', 'created_at']
    inlines = [PurchasedProductsInline]
