from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('modern_art', views.modern_art),
    path('classic_art', views.classic_art),
    path('abstraction', views.abstraction),
    path('portrait', views.Portrait),
    path('favorites', views.favorites),
    path('add_to_favorites', views.add_to_favorites)
]
