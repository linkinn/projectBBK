from django.contrib import admin
from .models import LogsLogin

# Register your models here.
@admin.register(LogsLogin)
class LogsLoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'ip', 'created_at')
    search_fields = ('user', 'ip',)
    ordering = ('id', 'type', 'ip')
    list_filter = ['created_at', 'type']
