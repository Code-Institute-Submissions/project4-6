from django.shortcuts import render
from .models import Restaurant

# Create your views here.

def restaurants(request):

    restaurants = Restaurant.objects.all()

    context = {
        'restaurants': restaurants,
    }

    return render(request, 'restaurants/restaurants.html', context)