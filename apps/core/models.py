from django.db import models


class LogsLogin(models.Model):
    user = models.CharField(max_length=150, default='anonymo', verbose_name='Usuario')
    type = models.CharField(max_length=15, verbose_name='Tipo')
    ip = models.GenericIPAddressField(protocol='both', default='127.0.0.1', blank=True, null=True, verbose_name='IP')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Logs de atutenticação'
        verbose_name = 'um log'

    def __str__(self):
        return f'{self.user} - {self.ip}'
