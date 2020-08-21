from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Restaurant
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def restaurants(request):

    restaurants = Restaurant.objects.all()
    search_query = None
    messages.error(request, "No input found, please enter search criteria!")
    if request.GET:
        if 'search_text' in request.GET:
            search_query = request.GET['search_text']
            if not search_query:
                messages.error(request, "No input found, please enter search criteria!")
                return redirect(reverse('restaurants'))

            queries = Q(name__icontains=search_query)
            restaurants = restaurants.filter(queries)

    context = {
        'restaurants': restaurants,
        'search_term': search_query,
    }
    return render(request, 'restaurants/restaurants.html', context)

def restaurant_details(request, restaurant_id):

    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    context = {
        'restaurant': restaurant,
    }

    return render(request, 'restaurants/restaurant_details.html', context)