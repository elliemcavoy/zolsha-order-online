from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Menu, SubCategory
from .forms import MenuForm


def all_menu(request):
    """ View to render the menu page """

    menu = Menu.objects.all()
    subcategories = None
    sort = None
    direction = None
    unselected = None
    if request.GET:
        if 'subcategory' in request.GET:
            subcats = request.GET['subcategory'].split(',')
            menu = menu.filter(subcategory__name__in=subcats)
            subcategories = SubCategory.objects.filter(name__in=subcats)
            for s in subcategories:
                cats = list(s.category.name.split(','))
                unselected = SubCategory.objects.filter(
                    category__name__in=cats).exclude(name__in=subcats)

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
                messages.error(request, "You didn't enter any \
                               search criteria!")
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


def add_menu_item(request):
    """ Add a menu item """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the restaurant can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully added product!')
            return redirect(reverse('restaurant_admin'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the\
                           form is valid.')
    else:
        form = MenuForm()

    template = 'menu/add_menu_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
