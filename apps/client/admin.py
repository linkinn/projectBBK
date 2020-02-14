from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Data', {
            'fields': (
                ('first_name', 'last_name',), 'phone', 'birth_date'
            ),
        }),
        ('Complementary Data', {
            'classes': ('collapse',),
            'fields': (
                ('rg', 'cpf'), 'address'
            ),
        })
    )
    raw_id_fields = ('address',)
    list_display = ('first_name', 'last_name',
                    'birth_date', 'phone', 'cpf', 'address')
    search_fields = ('first_name', 'phone', 'cpf')
    ordering = ('first_name',)
    list_filter = ['created_at']
