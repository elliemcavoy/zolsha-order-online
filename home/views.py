from django.shortcuts import render

# Create your views here.

def index(request):
    """ View to render the index page """
    return render(request, 'home/index.html')


def handler404(request, exception=None):
    return render(request, '404.html')