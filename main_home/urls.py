from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='main_home-home'),
    path('about/', views.about, name='main_home-about'),
    path('search/', views.searchresult, name='main_home-search')

]
