from django.contrib import admin
from .models import Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Provide Data', {
            "fields": (
                ('name', 'email'), 'cnpj', 'phone', 'address'
            ),
        }),
    )
    raw_id_fields = ('address',)
    list_display = ('name', 'cnpj', 'email', 'phone', 'address')
    search_fields = ('name', 'cnpj', 'email')
    ordering = ('name', 'email')
    list_filter = ['created_at']
