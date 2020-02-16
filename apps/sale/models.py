from django.db import models
from django.core.exceptions import ValidationError
from apps.client.models import Client
from apps.product.models import Product
from apps.paymentMethod.models import PaymentMethod
from apps.stock.models import Stock
import time
import logging


logger = logging.getLogger('django')


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Cliente')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, verbose_name='Metodo de Pagamento')
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='Total da Venda')
    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vendas'
        verbose_name = 'uma venda'

    def __str__(self):
        return self.client.first_name


class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT, verbose_name='Venda')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Produto')
    quantity = models.IntegerField(verbose_name='Quantidade')
    discount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Desconto')
    total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')
    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Produtos Vendidos'
        verbose_name = 'um produto vendido'

    def clean(self):
        stock = Stock.objects.get(product=self.product)
        if self.quantity > stock.amount:
            # logger.error(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {request.user} Something went wrong!')
            raise ValidationError(f'Estoque atual {self.product} e de {stock.amount}.')
