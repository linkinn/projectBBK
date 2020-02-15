from django.db import models


class Address(models.Model):
    cep = models.CharField(max_length=10, verbose_name='CEP')
    district = models.CharField(max_length=200, verbose_name='Bairro')
    street = models.CharField(max_length=200, verbose_name='Rua')
    country = models.CharField(max_length=100, verbose_name='País')
    uf = models.CharField(max_length=100, verbose_name='Estado')
    city = models.CharField(max_length=100, verbose_name='Cidade')
    complement = models.CharField(max_length=200, verbose_name='Complemento')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Endereço'
        verbose_name = 'um endereço'

    def __str__(self):
        return self.cep
