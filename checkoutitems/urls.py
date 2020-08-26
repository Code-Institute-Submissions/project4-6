from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkoutitems, name='checkoutitems'),
    path('checkout_completed/<order_number>', views.checkout_completed, name='checkout_completed'),
    path('cache_checkoutitems_data/', views.cache_checkoutitems_data, name='cache_checkoutitems_data'),
    path('wh/', webhook, name='webhook'),
]