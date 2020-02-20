from django.db import models
from apps.address.models import Address


class Client(models.Model):
    first_name = models.CharField(max_length=250, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=250, blank=True, null=True, verbose_name='Ultimo Nome')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    phone = models.CharField(max_length=15, verbose_name='Telefone')
    rg = models.CharField(max_length=9, unique=True, blank=True, null=True, verbose_name='RG')
    cpf = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name='CPF')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Endereço', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Clientes'
        verbose_name = 'um client'

    def __str__(self):
        return self.first_name
