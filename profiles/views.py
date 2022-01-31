from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from reservations.models import Reservation

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    if profile.orders:
        orders = profile.orders.all()
    else:
        orders = None
    
    if profile.reservation:
        reservation = profile.reservation.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'reservation': reservation,
    }

    return render(request, template, context)



def reorder(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    reorder_bag = order.original_bag
    lineitems = order.lineitems.all()
    bag = request.session.get('bag', {})
    for line in lineitems:
        item_id = line.item.id
        quantity = line.quantity
        option = line.item_option
        if line.item_option:
            bag[item_id] = {'items_by_option': {option: quantity}}
        else:
            bag[item_id] = quantity
        
    request.session['bag'] = bag
    redirect_url = request.POST.get('redirect_url')

    print(reorder_bag)
    

    return redirect(redirect_url)

