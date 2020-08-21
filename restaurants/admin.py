from django.contrib import admin
from .models import Restaurant, Cuisine, Location

class CuisineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'cuisine',
        'location',
        'discount',
        'price',
        'image',
    )

    ordering = ('name',)

# Register your models here.

admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
