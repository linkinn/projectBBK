from django.db import models


class PaymentMethod(models.Model):
    type_payment = models.CharField(max_length=120, verbose_name='Tipo de pagamento')
    mode = models.CharField(max_length=120, verbose_name='Modo de pagamento')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Metodo de pagamento'
        verbose_name = 'um metodo de pagamento'

    def __str__(self):
        return f'{self.type_payment} {self.mode}'
