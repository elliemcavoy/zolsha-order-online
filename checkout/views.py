from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51KCw7TAAKGESx0rhHCk3rVyF6OcqU8pHM6t8gHlK8BX4RTl4eNWpOMrwheAPaKO2VlscgrDSuuVjealLBtzfcyN000pZeFyEgz',
        'client_secret_key': 'test client secret'
    }

    return render(request, template, context)


