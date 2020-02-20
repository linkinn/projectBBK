from django.contrib import admin
from .models import Sale, SaleProduct


@admin.register(SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Produto Vendido', {
            "fields": (
                'sale', ('product', 'quantity', 'discount'), 'status', 'total'
            ),
        }),
    )
    readonly_fields = ('total',)
    list_display = ('id', 'sale', 'number_sale', 'product', 'quantity', 'total_payable', 'status')
    search_fields = ('sale__id', 'product__name', 'sale__client__first_name')
    ordering = ('id', 'quantity', 'total', 'status')
    list_filter = ['status', 'created_at']

    def number_sale(self, obj):
        number = f'N° {obj.sale.id}'
        return number

    def total_payable(self, obj):
        total = f'R$ {obj.total}'
        return total

    number_sale.short_description = 'Numero da venda'
    total_payable.short_description = 'total'


class SaleProductInline(admin.TabularInline):
    model = SaleProduct
    extra = 1
    readonly_fields = ('total',)


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Vendas', {
            "fields": (
                ('client', 'payment_method',), 'sale_date', 'status', 'total'
            ),
        }),
    )
    readonly_fields = ('total',)
    list_display = ('id', 'client', 'sale_date', 'payment_method', 'total_payable', 'status')
    search_fields = ('id', 'client', 'payment_method', 'total', 'status')
    ordering = ('id', 'total', 'status')
    list_filter = ['payment_method__type_payment', 'status', 'sale_date']
    inlines = [SaleProductInline]

    def total_payable(self, obj):
        total = f'R$ {obj.total}'
        return total

    total_payable.short_description = 'total'
