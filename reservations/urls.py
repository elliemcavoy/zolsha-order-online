from django.urls import path
from .views import TableReservation
from djreservation import urls as djreservation_urls

urlpatterns = [
    path('', TableReservation.as_view()),
] + djreservation_urls.urlpatterns