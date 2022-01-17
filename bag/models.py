from django.db import models


class DeliveryCharges(models.Model):
    class Meta:
        verbose_name_plural = 'DeliveryCharges'
        
    area = models.CharField(max_length=4, null=False, blank=False)
    charge = models.DecimalField(max_digits=6, decimal_places=2)
