from django.shortcuts import render, redirect, reverse, HttpResponse
from restaurants.models import Restaurant
from django.contrib import messages

# Create your views here.

def shoppingbag(request):
    return render(request, 'shoppingbag/shoppingbag.html')

def add_to_shoppingbag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    restaurant = Restaurant.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
    else:
        shoppingbag[item_id] = quantity
        messages.success(request, f'Added {restaurant.name} to your Shopping bag!')

    request.session['shoppingbag'] = shoppingbag
    print(request.session['shoppingbag'])
    print(shoppingbag.items())
    return redirect(redirect_url)

def update_shoppingbag(request, item_id):
    """ Update the shopping bag """

    quantity = int(request.POST.get('quantity'))
    shoppingbag = request.session.get('shoppingbag', {})

    """ if item_id in list(shoppingbag.keys()): """
    """        shoppingbag[item_id] = quantity """
    """else: """
    """ Update the quantity to the value specified in the quantity input box """

    shoppingbag[item_id] = quantity

    request.session['shoppingbag'] = shoppingbag
    print(request.session['shoppingbag'])
    print(shoppingbag.items())
    return redirect(reverse('shoppingbag'))

def remove_shoppingbag_item(request, item_id):
    """ Remove an item from the shopping bag """
    try:
        shoppingbag = request.session.get('shoppingbag', {})
        shoppingbag.pop(item_id)

        request.session['shoppingbag'] = shoppingbag
        print(request.session['shoppingbag'])
        print(shoppingbag.items())
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)