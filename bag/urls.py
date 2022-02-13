from django.urls import path 
from . import views

urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('delete/<item_id>/', views.delete_from_bag, name='delete_from_bag'),
]