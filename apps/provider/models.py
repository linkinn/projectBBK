from django.db import models
from apps.address.models import Address


class Provider(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    cnpj = models.CharField(max_length=18, unique=True, blank=True, null=True, verbose_name='CNPJ')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone')
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Endereço')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.name
