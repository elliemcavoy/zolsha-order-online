from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from menu.models import Menu


def shopping_bag(request):
    """Renders the shopping bag page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Adds the selected menu item to the shopping bag with the requested
       quantity and option if applicable."""

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
                messages.success(request, f'You updated {option.title()}\
                {item.name} quantity to \
                {bag[item_id]["items_by_option"][option]}')
            else:
                bag[item_id]['items_by_option'][option] = quantity
                messages.success(request, f'You added {option.title()}\
                {item.name} to your order')
        else:
            bag[item_id] = {'items_by_option': {option: quantity}}
            messages.success(request, f'You added {option.title()}\
            {item.name} to your order')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'You updated {item.name}\
            quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'You added {item.name} to your order')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the selected menu item to the specified amount"""

    item = get_object_or_404(Menu, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    option = None
    if 'item_option' in request.POST:
        option = request.POST['item_option']
    bag = request.session.get('bag', {})

    if option:
        if quantity > 0:
            bag[item_id]['items_by_option'][option] = quantity
            messages.success(request, f'Updated {option.title()} {item.name}\
            quantity to {bag[item_id]["items_by_option"][option]}')
        else:
            del bag[item_id]['items_by_option'][option]
            if not bag[item_id]['items_by_option']:
                bag.pop(item_id)
            messages.success(request, f'Removed {option.title()} {item.name}\
            from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {item.name} quantity to \
            {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {item.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def delete_from_bag(request, item_id):
    """Remove the menu item from the shopping bag"""

    try:
        item = get_object_or_404(Menu, pk=item_id)
        option = None
        if 'item_option' in request.POST:
            option = request.POST['item_option']
        bag = request.session.get('bag', {})

        if option:
            del bag[item_id]['items_by_option'][option]
            if not bag[item_id]['items_by_option']:
                bag.pop(item_id)
            messages.success(request, f'Removed {option.title()} {item.name}\
            from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {item.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
