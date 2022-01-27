from django.shortcuts import render, redirect, reverse
from djreservation.views import SimpleProductReservation
from .models import Reservation
from .forms import ReservationForm



def reservation(request):

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'time': request.POST['time'],
            'date': request.POST['date'],
            'covers': request.POST['covers'],
        }

        reservation_form = ReservationForm(form_data)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.save()

            return redirect(reverse('reservation_complete'))

    reservation_form = ReservationForm()
    template = 'reservations/reservation.html'
    context = {
        'reservation_form': reservation_form,
        
    }

    return render(request, template, context)

def reservation_complete(request):
    template = 'reservations/reservation-complete.html'
    return render(request, template, context)


   
