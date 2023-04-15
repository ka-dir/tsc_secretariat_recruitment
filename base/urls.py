from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('adverts/', views.adverts_page, name="adverts"),
    path('advert/<str:pk>/', views.advert_page, name="advert"),
]
