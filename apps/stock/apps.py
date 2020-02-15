from django.apps import AppConfig


class StockConfig(AppConfig):
    name = 'apps.stock'

    def ready(self):
        import apps.stock.signals
