from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppingbag, name='shoppingbag'),
    path('add/<item_id>/',
         views.add_to_shoppingbag, name='add_to_shoppingbag'),
    path('update/<item_id>/',
         views.update_shoppingbag, name='update_shoppingbag'),
    path('remove/<item_id>/',
         views.remove_shoppingbag_item, name='remove_shoppingbag_item'),
]
