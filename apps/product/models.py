from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Color(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Cor')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Referencia')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Referencias'

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=10, verbose_name='Tipo')
    value = models.CharField(max_length=30, verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Medidas'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Nome')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Preço')
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2,
                                         blank=True, null=True, verbose_name='Preço de Compra')
    weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Peso')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name='Cor')
    reference = models.ForeignKey(Reference, on_delete=models.PROTECT, verbose_name='Referencia')
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT, verbose_name='Medida')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.name} {self.reference} {self.color}'
