from django.contrib import admin
from .models import Office


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('id', 'name',)
    list_filter = ['created_at']
