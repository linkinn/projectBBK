from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# from apps.purchasedProducts.models import PurchasedProducts


class PurchasedProvider(models.Model):
    name = models.CharField(max_length=120, default='Desconhecido')
    note_number = models.IntegerField(unique=True)
    purchase_date = models.DateField()
    total = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Registrar Compras'

    def __str__(self):
        return self.name


# @receiver(pre_save)
# def update_total(sender, instance, **kwargs):
#     instance.total = PurchasedProducts.get_total()
