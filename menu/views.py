from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Menu

# Create your views here.

def all_menu(request):
    """ View to render the menu page """
    menu = Menu.objects.all()

    context = {
        'menu': menu,
    }
    return render(request, 'menu/menu.html', context)