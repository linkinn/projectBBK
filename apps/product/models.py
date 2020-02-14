from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Referencias'

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=10)
    value = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Medidas'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2,
                                         blank=True, null=True)
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    reference = models.ForeignKey(Reference, on_delete=models.PROTECT)
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.name} {self.reference} {self.color}'
