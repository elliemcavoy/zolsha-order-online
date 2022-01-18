from django.urls import path 
from . import views

urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    #path('calc_delivery/', views.calculate_delivery, name='calculate_delivery')
]