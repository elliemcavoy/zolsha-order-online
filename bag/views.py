from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from menu.models import Menu
# Create your views here.

def shopping_bag(request):

    return render(request, 'bag/bag.html')


#def add_to_bag(request, item_id):
 #   item = get_object_or_404(Menu, pk=item_id)
  #  quantity = int(request.POST.get('quantity'))
   # redirect_url = request.POST.get('redirect_url')
    #option = None
    #if 'item_option' in request.POST:
     #   option = request.POST['item_option']
    #bag = request.session.get('bag', {})
    #request.session['bag'] = bag
    
