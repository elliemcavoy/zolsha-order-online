from django.shortcuts import render

def checkout(request):
    """ View to render the index page """
    return render(request, 'checkout/checkout.html')


