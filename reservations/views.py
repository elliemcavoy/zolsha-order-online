from django.shortcuts import render
from djreservation.views import SimpleProductReservation
from .models import Reservation


# Create your views here.

class TableReservation(SimpleProductReservation):
    base_model = Reservation     # required
    amount_field = 'quantity'  # required
    max_amount_field = 'max_amount' # required
    extra_display_field = []  # not required

    def reservation(request):
    


        return render(request, 'reservations/reservation.html')
