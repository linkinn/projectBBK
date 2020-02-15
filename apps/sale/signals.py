from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import SaleProduct, Sale


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
