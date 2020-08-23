from django.shortcuts import render, redirect

# Create your views here.

def shoppingbag(request):
    return render(request, 'shoppingbag/shoppingbag.html')

def add_to_shoppingbag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
    else:
        shoppingbag[item_id] = quantity

    request.session['shoppingbag'] = shoppingbag
    print(request.session['shoppingbag'])
    print(shoppingbag.items())
    return redirect(redirect_url)