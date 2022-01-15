from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Menu

def bag_items(request):
    bag_items = []
    total = 0
    item_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        if isinstance(quantity, int):
            item = get_object_or_404(Menu, pk=item_id)
            subtotal = quantity * item.price
            total += quantity * item.price
            item_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'item': item,
                'subtotal': subtotal
            })
    delivery = 0
    grand_total = delivery + total
    context = {
        "bag_items":bag_items,
        "total": total,
        "delivery": delivery,
        "grand_total": grand_total
        #item_count
    }

    return context