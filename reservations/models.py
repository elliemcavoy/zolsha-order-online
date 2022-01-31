from django.db import models
import uuid
from profiles.models import UserProfile

# Create your models here.

class Reservation(models.Model):
    res_number = models.CharField(max_length=32, null=False, editable=False, default=0)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    covers = models.CharField(max_length=2, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='reservation')

    def _generate_res_number(self):
        
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        
        if not self.res_number:
            self.res_number = self._generate_res_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.res_number
    
