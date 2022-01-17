from django.contrib import admin
from .models import DeliveryCharges


class DeliveryChargesAdmin(admin.ModelAdmin):

    list_display = ('area', 'charge')


admin.site.register(DeliveryCharges, DeliveryChargesAdmin)