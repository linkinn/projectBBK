from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.exceptions import ValidationError
from apps.product.models import Product
from apps.purchaseProvider.models import PurchasedProducts
from apps.sale.models import SaleProduct
from .models import Stock


@receiver(post_save, sender=Product)
def create_stock(sender, instance, created, **kwargs):
    if created:
        Stock.objects.create(product=instance, amount=0)


@receiver(post_save, sender=PurchasedProducts)
def create_stock_purchases(sender, instance, created, **kwargs):
    stock = Stock.objects.get(product=instance.product)
    stock.amount += instance.quantity
    stock.save()


@receiver(pre_save, sender=SaleProduct)
def stock_sale_products_quantity(sender, instance, **kwargs):
    stock = Stock.objects.get(product=instance.product)
    sale_product = None

    if instance.id:
        sale_product = SaleProduct.objects.get(pk=instance.id)
    else:
        sale_product = instance

    if instance.status != sale_product.status and instance.status == False:
        stock.amount += sale_product.quantity
        stock.save()
        return
    elif instance.status != sale_product.status and instance.status:
        stock.amount -= instance.quantity
        stock.save()
        return

    if sale_product.quantity > instance.quantity:
        value = sale_product.quantity - instance.quantity
        stock.amount += value
        stock.save()
        return
    else:
        value = instance.quantity - sale_product.quantity
        stock.amount -= value
        stock.save()


@receiver(post_save, sender=SaleProduct)
def down_stock_sale_products(sender, instance, created, **kwargs):
    stock = Stock.objects.get(product=instance.product)
    if created:
        stock.amount -= instance.quantity
        stock.save()
