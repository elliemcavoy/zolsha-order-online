from decimal import Decimal
import json
import stripe

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from bag.contexts import bag_items
from profiles.models import UserProfile
from menu.models import Menu
from .models import Order, OrderLineItem, Offer
from .forms import OrderForm



@require_POST
def cache_checkout_data(request):
    """Saves bag metadata"""

    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    """Uses stripe & checkout form data to create a successful checkout"""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_bag = bag_items(request)
    warning=None
    order_total = current_bag['total']
    delivery_cost = 0

    if 'delivery_charge' in request.session:
        charge = request.session.get('delivery_charge')
        delivery_cost = Decimal(charge)        
    else: 
        warning=("Are you sure you want to collect?")
        
    if 'discount' in request.GET:
        order_total = current_bag['total']
        offer = Offer.objects.all()
        discount = request.GET['discount']
        discount_code = discount.upper()
        for o in offer: 
            if discount_code == o.offer_code:
                percent = o.discount/100
                discounted = order_total * percent
                order_total = order_total - discounted
            else:
                messages.error(request, 'Sorry, that is not a valid discount code.')
                
    else:
        order_total = current_bag['total']
                
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.delivery_cost = delivery_cost
            order.save()
            
            for item_id, quant in bag.items():
                try:
                    item = Menu.objects.get(id=item_id)
                    if isinstance(quant, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            item=item,
                            quantity=quant,
                        )
                        order_line_item.save()
                    else:
                        for option, quantity in quant['items_by_option'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                item=item,
                                quantity=quantity,
                                item_option=option,
                            )
                            order_line_item.save()
                except Menu.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        grand_total = order_total + delivery_cost
        stripe_total = round(grand_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'order_total': order_total,
        'grand_total': grand_total,
        'delivery_cost':delivery_cost,
        'warning': warning
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """Confirms order success, displays order confirmation 
        & saves order to user profile"""

    order = get_object_or_404(Order, order_number=order_number)
    
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    if 'delivery_charge' in request.session:
        del request.session['delivery_charge']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
