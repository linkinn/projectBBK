from django.db import models
from apps.product.models import Product


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, verbose_name='Produto')
    amount = models.IntegerField(verbose_name='Quantidade')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Estoque'

    def get_total(self):
        total = self.product.price * self.amount
        return total

    def __str__(self):
        return self.product.name
