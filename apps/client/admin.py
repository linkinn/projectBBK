from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados do cliente', {
            'fields': (
                ('first_name', 'last_name',), 'phone', 'birth_date', 'address'
            ),
        }),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': (
                ('rg', 'cpf'),
            ),
        })
    )
    raw_id_fields = ('address',)
    list_display = ('id', 'get_fullname', 'birth_date',
                    'phone', 'cpf', 'address')
    search_fields = ('first_name', 'phone', 'cpf')
    ordering = ('id', 'first_name',)
    list_filter = ['created_at']

    def get_fullname(self, obj):
        full_name = f'{obj.first_name} {obj.last_name}'
        return full_name

    get_fullname.short_description = 'Full Name'
