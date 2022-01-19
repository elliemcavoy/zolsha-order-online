from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Upper
from menu.models import Menu
from .models import DeliveryCharges
# Create your views here.

def shopping_bag(request):

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    item = get_object_or_404(Menu, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    option = None
    if 'item_option' in request.POST:
        option = request.POST['item_option']
    bag = request.session.get('bag', {})

    if option:
        if item_id in list(bag.keys()):
            if option in bag[item_id]['items_by_option'].keys():
                bag[item_id]['items_by_option'][option] += quantity
                messages.success(request, f'Updated {option.title()} {item.name} quantity to {bag[item_id]["items_by_option"][option]}')
            else:
                bag[item_id]['items_by_option'][option] = quantity
                messages.success(request, f'Added {option.title()} {item.name} to your order')
        else:
            bag[item_id] = {'items_by_option': {option: quantity}}
            messages.success(request, f'Added {option.title()} {item.name} to your order')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {item.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {item.name} to your order')


    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)



   



    

    



