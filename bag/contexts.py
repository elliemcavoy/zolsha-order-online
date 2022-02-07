from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Menu
from django.db.models.functions import Upper
from .models import DeliveryCharges

def bag_items(request):
    basket_items = []
    total = 0
    item_count = 0
    delivery_charge = 0
    bag = request.session.get('bag', {})

    for item_id, quant in bag.items():
        print(f"BAG: {bag}")
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
        
        if not delivery_postcode:
            messages.error(request, "Please enter your postcode.")
            return redirect(reverse('shopping_bag'))
        for c in charge: 
            if delivery_postcode.__contains__(c.area):
                delivery_charge = c.charge
    else:
        delivery_charge = 0

    grand_total = delivery_charge + total
    context = {
        "bag_items": basket_items,
        "total": total,
        "grand_total": grand_total,
        "item_count": item_count,
        "delivery_charge" : delivery_charge,
    }

    return context