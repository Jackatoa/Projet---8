from django.urls import path
from . import views
from .views import SavedListView, AlimentDeleteView
def trigger_error(request):
    division_by_zero = 1 / 0
urlpatterns = [
    path('', views.home, name='main_home-home'),
    path('aliment/', views.aliment, name='main_home-aliment'),
    path('search/', views.search, name='main_home-search'),
    path('proposition/', views.proposition, name='main_home-proposition'),
    path('saved/', SavedListView.as_view(), name='main_home-saved'),
    path('confirmation/', views.confirmation, name='main_home-confirmation'),
    path('infosaved/', views.infosaved, name='main_home-infosaved'),
    path('delete/', views.delete, name='main_home-delete'),
    path('validatedelete/', views.validatedelete, name='main_home-validatedelete'),
    path('mention/', views.mention, name='main_home-mention'),
    path('sentry-debug/', trigger_error),
]
