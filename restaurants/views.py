from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Restaurant, Location, Cuisine
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import RestaurantForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def restaurants(request):

    restaurants = Restaurant.objects.all()
    search_query = None
    this_location = None
    this_cuisine = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sort_item = request.GET['sort']
            sort = sort_item
            if sort_item == 'name':
                sort_item = 'lower_name'
                restaurants = restaurants.annotate(lower_name=Lower('name'))

            if sort_item == 'cuisine':
                sort_item = 'cuisine__name'

            if sort_item == 'location':
                sort_item = 'location__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_item = f'-{sort_item}'
            restaurants = restaurants.order_by(sort_item)

        if 'location' in request.GET:
            this_location = request.GET['location'].split(',')
            restaurants = restaurants.filter(location__name__in=this_location)
            this_location = Location.objects.filter(name__in=this_location)

        if 'cuisine' in request.GET:
            this_cuisine = request.GET['cuisine'].split(',')
            print(this_cuisine)
            restaurants = restaurants.filter(cuisine__name__in=this_cuisine)
            this_cuisine = Cuisine.objects.filter(name__in=this_cuisine)

        if 'search_text' in request.GET:
            search_query = request.GET['search_text']
            if not search_query:
                messages.error(
                    request, "No input found, please enter search criteria!")
                return redirect(reverse('restaurants'))

            queries = Q(name__icontains=search_query)
            restaurants = restaurants.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'restaurants': restaurants,
        'search_term': search_query,
        'current_location': this_location,
        'current_cuisine': this_cuisine,
        'current_sorting': current_sorting,
    }
    return render(request, 'restaurants/restaurants.html', context)


def restaurant_details(request, restaurant_id):

    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    context = {
        'restaurant': restaurant,
    }

    return render(request, 'restaurants/restaurant_details.html', context)


@login_required
def add_restaurant(request):
    """ Add a restaurant to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save()
            messages.success(request, 'Successfully added restaurant!')
            return redirect(
                reverse('restaurant_details', args=[restaurant.id]))
        else:
            messages.error(
                request, 'Add Failed. Please ensure the form is valid.')
    else:
        form = RestaurantForm()

    template = 'restaurants/add_restaurant.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_restaurant(request, restaurant_id):
    """ Update a resturant in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated restaurant!')
            return redirect(
                reverse('restaurant_details', args=[restaurant.id]))
        else:
            messages.error(request, 'Failed to update restaurant. Please ensure the form is valid.')
    else:
        form = RestaurantForm(instance=restaurant)
        messages.info(request, f'You are editing {restaurant.name}')

    template = 'restaurants/update_restaurant.html'
    context = {
        'form': form,
        'restaurant': restaurant,
    }

    return render(request, template, context)


@login_required
def remove_restaurant(request, restaurant_id):
    """ Remove a restaurant from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    restaurant.delete()
    messages.success(request, 'Restaurant deleted!')
    return redirect(reverse('restaurants'))


def rest(request):

    rest = Restaurant.objects.all()

    context = {
        'rest': rest,
    }

    return render(request, 'restaurants/rest.html', context)
