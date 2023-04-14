from django.shortcuts import render

# Create your views here.


def dashboard_page(request):
    context = {}
    return render(request, 'base/dashboard.html', context)


def combined_page(request):
    return render(request, 'base/combined.html')
