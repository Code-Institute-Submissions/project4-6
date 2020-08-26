from django.apps import AppConfig


class CheckoutitemsConfig(AppConfig):
    name = 'checkoutitems'

    def ready(self):
        import checkoutitems.signals