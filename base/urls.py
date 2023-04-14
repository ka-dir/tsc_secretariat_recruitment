from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard_page, name="dashboard"),
    path('combined/', views.combined_page, name="combined"),
]