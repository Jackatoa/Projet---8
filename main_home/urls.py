from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='main_home-home'),
    path('search/', views.search, name='main_home-search'),
    path('saved/', views.saved, name='main_home-saved'),
    path('aliment/', views.aliment, name='main_home-aliment')

]
