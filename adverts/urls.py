from django.urls import path
from . import views

urlpatterns = [
    path('adverts/', views.adverts_page, name="adverts")
]
