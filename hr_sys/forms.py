from django.forms import ModelForm
from base.models import Advert


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = '__all__'
