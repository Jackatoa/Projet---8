from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='main_home-home'),
    path('aliment/', views.aliment, name='main_home-aliment'),
    path('search/', views.search, name='main_home-search'),
    path('proposition/', views.proposition, name='main_home-proposition'),
    path('saved/', views.saved, name='main_home-saved'),


]
