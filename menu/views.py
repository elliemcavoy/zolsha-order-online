from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Menu, Category, SubCategory

# Create your views here.

def all_menu(request):
    """ View to render the menu page """
    menu = Menu.objects.all()
    subcategories = None
    sort = None
    direction = None
    
    if request.GET:
        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory'].split(',')
            menu = menu.filter(subcategory__name__in=subcategories)
            subcategories = SubCategory.objects.filter(name__in=subcategories)
            unselected = SubCategory.objects.filter().exclude(name__in=subcategories)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                menu = menu.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            menu = menu.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('menu'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            menu = menu.filter(queries)
        
    current_sorting = f'{sort}_{direction}'

    context = {
        'menu': menu,
        'selected_categories': subcategories,
        'unselected_categories': unselected,
        'current_sorting': current_sorting,
    }
    return render(request, 'menu/menu.html', context)
