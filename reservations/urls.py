from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('complete', views.reservation_complete, name='reservation_complete'),
    path('check_availability', views.check_availability, name='check_availability'),
    
]