from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkoutitems, name='checkoutitems')
]