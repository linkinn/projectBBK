from django.db import models
from apps.address.models import Address


class Company(models.Model):
    fantasy_name = models.CharField(max_length=200, unique=True)
    social_registration = models.CharField(
        max_length=40, unique=True, null=True, blank=True)
    cnpj = models.CharField(max_length=18, unique=True)
    state_registration = models.CharField(
        max_length=20, unique=True, null=True, blank=True)
    open_date = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='company', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Empresa'

    def __str__(self):
        return self.fantasy_name
