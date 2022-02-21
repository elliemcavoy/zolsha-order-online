from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.contrib import messages
from menu.models import Menu
from .models import DeliveryCharges


def bag_items(request):
    """Adds items to the shopping bag"""

    basket_items = []
    total = 0
    item_count = 0
    charge = request.session.get('delivery_charge')
    if 'delivery_charge' in request.session:
        delivery_charge = Decimal(charge)
    else:
        delivery_charge = 0
    bag = request.session.get('bag', {})

    for item_id, quant in bag.items():
        if isinstance(quant, int):
            item = get_object_or_404(Menu, pk=item_id)
            total += quant * item.price
            item_count += quant
            basket_items.append({
                'item_id': item_id,
                'quantity': quant,
                'item': item,
            })
        else:
            item = get_object_or_404(Menu, pk=item_id)
            for option, quantity in quant['items_by_option'].items():
                total += quantity * item.price
                item_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'item': item,
                    'option': option,
                })
    if 'postcode' in request.GET:
        charge = DeliveryCharges.objects.all()
        postcode = request.GET['postcode']
        delivery_postcode = postcode.upper()
        plist = []
        attempt = 1
        while attempt <= 4:
            for c in charge:
                if delivery_postcode.__contains__(c.area):
                    delivery_charge = c.charge
                    dcharge = 1
                    attempt += 1
                    request.session['delivery_charge'] = str(delivery_charge)
                elif not delivery_postcode.__contains__(c.area):
                    dcharge = 0
                    attempt += 1

                    plist.append(dcharge)

                    if attempt == 4:
                        final_list = sum(plist)
                        if final_list == 0:
                            messages.error(request, 'Sorry\
                            we do not deliver here')

    grand_total = delivery_charge + total

    context = {
        "bag_items": basket_items,
        "total": total,
        "grand_total": grand_total,
        "item_count": item_count,
        "delivery_charge": delivery_charge
    }

    return context
