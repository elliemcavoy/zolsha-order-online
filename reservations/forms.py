from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('full_name', 'email', 'phone_number',
                  'date',
                  'time', 'covers')

    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

        self.fields['date'].widget.attrs['class'] = 'datepicker'
        self.fields['time'].widget.attrs['class'] = 'timepicker'
        self.fields['date'].widget.attrs['name'] = 'date'
        self.fields['time'].widget.attrs['name'] = 'time'
