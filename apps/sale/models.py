from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from apps.client.models import Client
from apps.product.models import Product
from apps.paymentMethod.models import PaymentMethod


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Cliente')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, verbose_name='Metodo de Pagamento')
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='Total da Venda')
    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vendas'

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


@receiver(pre_save, sender=SaleProduct)
def before_save_sale_product_total(sender, instance, **kwargs):
    total = (instance.product.price * instance.quantity) - instance.discount
    instance.total = total


@receiver(post_save, sender=SaleProduct)
def before_save_sale_total(sender, instance, created, **kwarg):
    total = 0
    current_sale = Sale.objects.get(id=instance.sale.id)
    sales = SaleProduct.objects.filter(sale=current_sale)
    for sale in sales:
        total += sale.total
    current_sale.total = total
    current_sale.save()
