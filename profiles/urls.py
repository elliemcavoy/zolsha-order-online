from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('reorder/<order_number>/', views.reorder, name='reorder'),
    path('restaurant-admin/', views.restaurant_admin, name='restaurant_admin'),

    
]