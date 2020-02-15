from django.contrib import admin
from .models import PaymentMethod


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Registrar metodo de pagamento', {
            "fields": (
                ('type_payment', 'mode'),
            ),
        }),
    )

    list_display = ('type_payment', 'mode')
    search_fields = ('type_payment',)
    ordering = ('type_payment',)
    list_filter = ['mode']
