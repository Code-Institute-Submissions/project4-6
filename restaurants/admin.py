from django.contrib import admin
from .models import Restaurant, Cuisine, Location

# Register your models here.

admin.site.register(Cuisine)
admin.site.register(Location)
admin.site.register(Restaurant)

