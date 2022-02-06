from django.contrib import admin
from .models import Order, OrderLineItem, Offer

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    list_display = ('order_number', 'order_date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('offer_code', 'discount',)




admin.site.register(Order, OrderAdmin)
admin.site.register(Offer, OfferAdmin)

