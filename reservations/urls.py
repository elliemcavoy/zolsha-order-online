from django.urls import path
from . import views
from djreservation import urls as djreservation_urls

urlpatterns = [
    path('', views.reservation, name='reservation' ),
] + djreservation_urls.urlpatterns