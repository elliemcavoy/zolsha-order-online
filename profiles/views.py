from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from reservations.models import Reservation
import datetime

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

    messages.success(request, f'Thank you for re-ordering')
        
    request.session['bag'] = bag
    redirect_url = request.POST.get('redirect_url')

    print(reorder_bag)
    

    return redirect(redirect_url)

@login_required
def restaurant_admin(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the restaurant can do that.')
        return redirect(reverse('home'))
    orders = Order.objects.all()
    reservations = Reservation.objects.all()
    today = datetime.date.today()
    todays_date = today.strftime("%Y-%m-%d")
    print(todays_date)
    order_filtered = Q(order_date__icontains=todays_date)
    res_filtered = Q(date__icontains=todays_date)
    orders = orders.filter(order_filtered)
    reservations = reservations.filter(res_filtered)
    
    print(orders)


    template = 'profiles/restaurant-admin.html'
    context = {
         'orders': orders,
         'reservations': reservations,
        }
    return render(request, template, context)
