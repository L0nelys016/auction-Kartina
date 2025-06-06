from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('modern_art', views.modern_art),
    path('classic_art', views.classic_art),
    path('abstraction', views.abstraction),
    path('portrait', views.Portrait),
    path('favorites', views.favorites),
    path('add_to_favorites', views.add_to_favorites),
    path('remove_from_favorites', views.remove_from_favorites),
    path('my_picture', views.my_picture, name='my_picture'),
    path('add_pic', views.add_pic),
    path('delete_picture', views.delete_picture, name='delete_picture'),
    path('register/', views.register_view, name='register'),
    path('login',  views.login_view, name='login'),
    path('logout',  views.logout_view, name='logout'),
    path('profile',  views.profile_view, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
