from django.shortcuts import render
from djreservation.views import SimpleProductReservation
from .models import Reservation
from .forms import ReservationForm



def reservation(request):


    reservation_form = ReservationForm()

    
    template = 'reservations/reservation.html'
    context = {
        'reservation_form': reservation_form,
        
    }

    return render(request, template, context)

    


   
