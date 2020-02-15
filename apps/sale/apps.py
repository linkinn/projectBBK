from django.apps import AppConfig


class SaleConfig(AppConfig):
    name = 'apps.sale'

    def ready(self):
        import apps.sale.signals
