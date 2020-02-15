from django.db import models


class PaymentMethod(models.Model):
    type_payment = models.CharField(max_length=120)
    mode = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Metodo de pagamento'

    def __str__(self):
        return f'{self.type_payment} {self.mode}'
