from django.db import models


class Address(models.Model):
    cep = models.CharField(max_length=10)
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    complement = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.cep
