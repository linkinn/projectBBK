from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Current Company', {
            "fields": (
                ('cnpj', 'fantasy_name'), ('social_reason',
                                           'state_registration'), 'open_date', 'address', 'logo'
            ),
        }),
    )
    raw_id_fields = ('address',)
    list_display = ('id', 'fantasy_name', 'social_reason',
                    'cnpj', 'state_registration', 'open_date', 'address')
    search_fields = ('fantasy_name', 'cnpj')
