from django.urls import path
from . import views

urlpatterns = [
    path('adverts/', views.adverts_page, name="adverts"),
    path('advert/<str:pk>/', views.advert_page, name="advert"),
]
