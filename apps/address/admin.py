from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Endereço Atual', {
            "fields": (
                'cep', ('district', 'street'), 'complement'
            ),
        }),
        ('Nacionalidade', {
            # 'classes': ('collapse',),
            "fields": (
                ('country', 'uf', 'city'),
            )
        })
    )
    list_display = ('id', 'country', 'uf', 'city', 'cep', 'district', 'street')
    ordering = ('id', 'country', 'uf', 'city')
    search_fields = ('country', 'uf', 'city', 'cep')
    list_filter = ('country', 'uf', 'city')
