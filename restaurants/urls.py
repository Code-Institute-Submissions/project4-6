from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('<restaurant_id>', views.restaurant_details, name='restaurant_details'),
]