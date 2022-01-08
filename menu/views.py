from django.shortcuts import render

# Create your views here.

def menu(request):
    """ View to render the menu page """
    return render(request, 'menu/menu.html')