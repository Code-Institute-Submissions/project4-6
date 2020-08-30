from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('<int:restaurant_id>/', views.restaurant_details, name='restaurant_details'),
    path('add/', views.add_restaurant, name='add_restaurant'),
    path('update/<int:restaurant_id>/', views.update_restaurant, name='update_restaurant'),
    path('remove/<int:restaurant_id>/', views.remove_restaurant, name='remove_restaurant'),
]