from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.provider.models import Provider
from apps.product.models import Product
# from apps.purchasedProducts.models import PurchasedProducts


class PurchasedProvider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT, verbose_name='Fornecedor')
    note_number = models.IntegerField(unique=True, verbose_name='Numero da Nota')
    purchase_date = models.DateField(verbose_name='Data da Compra')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Compras'

    def __str__(self):
        return self.provider.name

    def total_purchased(self):
        total = 0
        purchases = PurchasedProducts.objects.filter(purchased_provider=self)
        for purchase in purchases:
            total += purchase.price

        return total


class PurchasedProducts(models.Model):
    PURCHASE_TYPE = [
        ('Avulso', 'Avulso'),
        ('NFE', 'Nota Fiscal')
    ]
    purchased_provider = models.ForeignKey(PurchasedProvider, on_delete=models.PROTECT, verbose_name='Fornecedor')
    purchase_type = models.CharField(max_length=15, choices=PURCHASE_TYPE, verbose_name='Tipo da Compra')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Produto')
    quantity = models.IntegerField(verbose_name='Quantidade')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Preço')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Produtos Comprado'
