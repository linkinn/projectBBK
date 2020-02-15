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

    list_display = ('id', 'type_payment', 'mode')
    search_fields = ('type_payment',)
    ordering = ('id', 'type_payment',)
    list_filter = ['mode']
