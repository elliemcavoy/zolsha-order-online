from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    list_display = ('order_number', 'order_date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)


admin.site.register(Order, OrderAdmin)
