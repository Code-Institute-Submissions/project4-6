from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from shoppingbag.contexts import shoppingbag_contents
import stripe


def checkoutitems(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    shoppingbag = request.session.get('shoppingbag', {})
    if not shoppingbag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('restaurants'))

    current_shoppingbag = shoppingbag_contents(request)
    total = current_shoppingbag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    if not stripe_secret_key:
        messages.warning(request, 'Stripe secret key is missing. \
            Did you forget to set it in your environment?')

    order_form = OrderForm()
    template = 'checkoutitems/checkoutitems.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)