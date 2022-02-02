from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.all_menu, name='all_menu'),
    path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
]