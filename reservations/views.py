from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .models import Reservation
from .forms import ReservationForm
from profiles.models import UserProfile
from django.db.models import Q

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
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                reservation_form = ReservationForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                reservation_form = ReservationForm()
        else:
            reservation_form = ReservationForm()

    template = 'reservations/reservation.html'
    context = {
        'reservation_form': reservation_form,
        
    }

    return render(request, template, context)


def reservation_complete(request):
    template = 'reservations/reservation-complete.html'
    context={
        
    }
    return render(request, template, context)


def check_availability(request):
    
    if request.GET:

        if 'date' in request.GET:
            date = request.GET['date']
        if 'time' in request.GET:
            time = request.GET['time']

        
            print(date)
            print(time)
            datetime = Q(date__icontains=date) & Q(time__icontains=time)
            existing_reservations = Reservation.objects.filter(datetime)
            resnumber=existing_reservations.count()
            print(resnumber)
            if resnumber >= settings.RESERVATION_THRESHOLD:
                print('no avail')
                messages.success(request, "Sorry we have no tables available, please pick a different time/date.")
            else:
                print('success')
        else:
            messages.error(request, 'Please select a date')
    
    reservation_form = ReservationForm()
    template = 'reservations/check_availability.html'
    context={
        'reservation_form': reservation_form
    }
    return render(request, template, context)
   
