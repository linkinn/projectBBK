from django.db import models
from apps.address.models import Address


class Company(models.Model):
    fantasy_name = models.CharField(max_length=200, unique=True, verbose_name='Nome Fantasia')
    social_reason = models.CharField(
        max_length=250, unique=True, null=True, blank=True, verbose_name='Razão Social')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    state_registration = models.CharField(
        max_length=20, unique=True, null=True, blank=True, verbose_name='Inscrição Estadual')
    open_date = models.DateField(verbose_name='Data de Abertura')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Endereço')
    logo = models.ImageField(upload_to='company', null=True, blank=True, verbose_name='Logo da Empresa')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Empresa'
        verbose_name = 'uma empresa'

    def __str__(self):
        return self.fantasy_name
