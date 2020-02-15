from django.db import models


class Office(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Cargo')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cargos'
        verbose_name = 'um cargo'

    def __str__(self):
        return self.name
