from django.shortcuts import get_object_or_404
from restaurants.models import Restaurant


def shoppingbag_contents(request):

    shoppingbag_items = []
    total = 0
    restaurant_count = 0
    shoppingbag = request.session.get('shoppingbag', {})

    for item_id, quantity in shoppingbag.items():
        restaurant = get_object_or_404(Restaurant, pk=item_id)
        print(restaurant)
        total += quantity * restaurant.price
        restaurant_count += quantity
        shoppingbag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'restaurant': restaurant,
        })

    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'restaurant_count': restaurant_count,
    }

    return context
