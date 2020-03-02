from django.contrib import admin
from .models import PurchasedProvider, PurchasedProducts


@admin.register(PurchasedProducts)
class PurchasedProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'purchased_provider', 'number_purchased',
                    'purchase_type', 'product', 'quantity', 'price')
    search_fields = ('purchased_provider__provider__name', 'product__name', 'purchased_provider__note_number')
    ordering = ('purchased_provider__purchase_date', 'price', 'quantity')
    list_filter = ['purchased_provider__purchase_date', 'created_at']
    actions = None

    def number_purchased(self, obj):
        number = f'N° {obj.purchased_provider.id}'
        return number

    number_purchased.short_description = 'Numero da compra'


class PurchasedProductsInline(admin.TabularInline):
    model = PurchasedProducts
    extra = 1


@admin.register(PurchasedProvider)
class PurchasedProviderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Shopping', {
            "fields": (
                ('provider', 'note_number'), 'purchase_date',
            ),
        }),
    )
    # readonly_fields = ('total',)
    list_display = ('id', 'provider', 'note_number', 'purchase_date', 'total_purchased')
    search_fields = ('provider', 'note_number')
    ordering = ('id', 'purchase_date',)
    list_filter = ['purchase_date', 'created_at']
    inlines = [PurchasedProductsInline]

    def total_purchased(self, obj):
        total = f'R$ {obj.total_purchased()}'
        return total

    total_purchased.short_description = 'total'
