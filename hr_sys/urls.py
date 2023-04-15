from django.urls import path
from . import views

urlpatterns = [
    path('adverts/', views.adverts, name="adverts"),
    path('create-advert', views.create_advert, name="create-advert"),
    path('update-advert/<str:pk>/', views.update_advert, name="update-advert"),
    path('delete-advert/<str:pk>/', views.delete_advert, name="delete-advert"),
]