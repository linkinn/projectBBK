from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Current Address', {
            "fields": (
                'cep', ('district', 'street')
            ),
        }),
        ('Nationality', {
            # 'classes': ('collapse',),
            "fields": (
                ('country', 'uf', 'city'),
            )
        })
    )
    list_display = ('country', 'uf', 'city', 'cep', 'district', 'street')
    ordering = ('country', 'uf', 'city')
    search_fields = ('country', 'uf', 'city', 'cep')
    list_filter = ('country', 'uf', 'city')
