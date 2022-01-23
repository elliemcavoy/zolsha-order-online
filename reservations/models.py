from django.db import models

# Create your models here.

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    covers = models.CharField(max_length=2, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    
