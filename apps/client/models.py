from django.db import models
from apps.address.models import Address


class Client(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    rg = models.CharField(max_length=9, unique=True, blank=True, null=True)
    cpf = models.CharField(max_length=15, unique=True, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
