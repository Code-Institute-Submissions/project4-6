from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppingbag, name='shoppingbag'),
    path('add/<item_id>/', views.add_to_shoppingbag, name='add_to_shoppingbag'),
]
