from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('<int:restaurant_id>/', views.restaurant_details, name='restaurant_details'),
    path('add/', views.add_restaurant, name='add_restaurant'),
]