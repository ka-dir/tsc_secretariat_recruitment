from django.shortcuts import render

# Create your views here.


def adverts_page(request):
    context = {}
    return render(request, 'adverts/adverts.html', context)
