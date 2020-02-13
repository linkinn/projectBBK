from django.contrib import admin
from .models import Product, Reference, Measure, Color


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product Data', {
            "fields": (
                'name', ('price', 'weight'), 'description', ('color',
                                                             'reference'), 'measure'
            ),
        }),
    )

    list_display = ('name', 'description', 'price',
                    'weight', 'color', 'reference', 'measure')
    search_fields = ('name', 'price', 'color', 'reference')
    ordering = ('name', 'price', 'weight', 'color')
    list_filter = ['color__name', 'reference__name']


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )
    list_filter = ['created_at']


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name', )
    ordering = ('name', )
    list_filter = ['created_at']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )
    list_filter = ['created_at']
