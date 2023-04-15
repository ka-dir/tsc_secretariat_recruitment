from django.shortcuts import render
from .models import Advert


# Create your views here.


def dashboard_page(request):
    context = {}
    return render(request, 'base/dashboard.html', context)


# Create your views here.


def adverts_page(request):
    adverts = Advert.objects.all
    context = {'adverts': adverts}
    return render(request, 'base/adverts.html', context)


def advert_page(request, pk):
    advert = Advert.objects.get(id=pk)
    context = {'advert': advert}
    return render(request, 'base/advert.html', context)
