from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.provider.models import Provider
# from apps.purchasedProducts.models import PurchasedProducts


class PurchasedProvider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    note_number = models.IntegerField(unique=True)
    purchase_date = models.DateField()
    total = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Registrar Compras'

    def __str__(self):
        return self.provider.name
