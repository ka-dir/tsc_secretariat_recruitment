from django.shortcuts import render, redirect
from base.views import Advert
from .forms import AdvertForm
from django.contrib import messages


# Create your views here.

def adverts(request):
    adverts = Advert.objects.all()
    context = {'adverts': adverts}
    return render(request, 'hr_sys/adverts.html', context)


# creating new advert
def create_advert(request):
    advert_form = AdvertForm()
    if request.method == 'POST':
        advert_form = AdvertForm(request.POST)
        if advert_form.is_valid():
            advert_form.save()
            messages.success(request, "Advert saved successfully")
            return redirect('adverts')
        else:
            messages.error(request, "Oops! error occurred while saving advert")
            return redirect('adverts')
    context = {'advert_form': advert_form}
    return render(request, 'hr_sys/advert-form.html', context)


# updating  advert
def update_advert(request, pk):
    advert = Advert.objects.get(id=pk)
    advert_form = AdvertForm(instance=advert)
    if request.method == 'POST':
        advert_form = AdvertForm(request.POST, instance=advert)
        if advert_form.is_valid():
            advert_form.save()
            messages.warning(request, "Advert updated successfully")
            return redirect('adverts')
        else:
            messages.error(request, "Oops! error occurred while updating advert")
            return redirect('adverts')
    context = {'advert_form': advert_form}
    return render(request, 'hr_sys/advert-form.html', context)


# delete advert
def delete_advert(request, pk):
    advert = Advert.objects.get(id=pk)
    if request.method == 'POST':
        advert.delete()
        messages.debug(request, "Advert deleted successfully")
        return redirect('adverts')
    context = {'advert': advert}
    return render(request, 'hr_sys/delete-form.html', context)
