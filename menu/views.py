from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Menu, Category, SubCategory

# Create your views here.

def all_menu(request):
    """ View to render the menu page """
    menu = Menu.objects.all()
    subcategories = None
   
    #for item in menu:
        #menu_item = get_object_or_404(Menu, pk=item_id)

    
    
    if request.GET:
        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory']
            menu = menu.filter(subcategory__name__in=subcategories)
            #categories = SubCategory.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('menu'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            menu = menu.filter(queries)

        

    context = {
        'menu': menu,
        'selected_categories': subcategories,
    }
    return render(request, 'menu/menu.html', context)
