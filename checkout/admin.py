from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    list_display = ('order_number', 'order_date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)




admin.site.register(Order, OrderAdmin)

