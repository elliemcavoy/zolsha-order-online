from django.urls import path 
from . import views

urlpatterns = [
    path('', views.all_menu, name='all_menu'),
    path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
    path('display_edit_menu/', views.display_edit_menu, name='display_edit_menu'),
    path('edit_menu_item/<item_id>/', views.edit_menu_item, name='edit_menu_item'),
]