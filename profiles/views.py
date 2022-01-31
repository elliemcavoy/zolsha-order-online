from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    #if profile.orders:
        #orders = profile.orders.all()
    #else:
    orders= profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)



def reorder(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    reorder_bag = order.original_bag
    lineitems = order.lineitems.all()
    for line in lineitems:
        print(line.item.id)
    
    redirect_url = request.POST.get('redirect_url')

    print(reorder_bag)
    

    return redirect(redirect_url)

