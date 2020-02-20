from django.dispatch import receiver
from django.db.models.signals import post_save
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


@receiver(post_save, sender=SaleProduct)
def down_stock_sale_products(sender, instance, created, **kwargs):
    if (instance.status):
        stock = Stock.objects.get(product=instance.product)
        stock.amount -= instance.quantity
        if (stock.amount < 0):
            return
    else:
        stock = Stock.objects.get(product=instance.product)
        stock.amount += instance.quantity
    stock.save()
