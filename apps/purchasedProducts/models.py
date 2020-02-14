from django.db import models
from apps.product.models import Product
from apps.purchaseProvider.models import PurchasedProvider


class PurchasedProducts(models.Model):
    PURCHASE_TYPE = [
        ('Avulso', 'Avulso'),
        ('NFE', 'Nota Fiscal')
    ]
    purchased_provider = models.ForeignKey(PurchasedProvider, on_delete=models.PROTECT)
    purchase_type = models.CharField(max_length=15, choices=PURCHASE_TYPE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Compras'

    def get_total(self):
        total = 0
        for product in self.product.all():
            total += product.purchase_price

        return total
