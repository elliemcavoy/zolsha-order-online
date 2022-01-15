from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from menu.models import Menu
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
        
        bag[item_id] = {'items_by_option': {option: quantity}}
        messages.success(request, f'Added {option.title()} {item.name} to your order')
    
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {item.name} to your order')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
    
