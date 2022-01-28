from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    
    list_display = ('full_name', 'email', 'phone_number',
                    'date',
                    'time', 'covers')




admin.site.register(Reservation)
