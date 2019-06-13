from django.shortcuts import render, redirect
from .models import Aliment
from .function import get_results


# Create your views here.

def home(request):
    query = request.GET.get('query')
    print(query)
    if query:
        context = {'foods': get_results(query)}
        return render(request, 'main_home/search.html', context, {'title': 'Résultats'})

    return render(request, 'main_home/home.html')


def saved(request):
    return render(request, 'main_home/saved.html')


def search(request):
    return render(request, 'main_home/search.html', {'title': 'Résultats'})


def aliment(request):
    aliment = {
        'name': 'Ratatouille RatatouilleRatatouille RatatouilleRatatouille RatatouilleRatatouille',
        'img': 'https://static.openfoodfacts.org/images/products/341/229/007/1788'
               '/front_fr.4.400.jpg', 'nutriscore': 'nutri', 'nutriletter': 'A',
        'url': 'https://world.openfoodfacts.org/product/3017230000059/olives-confites'
               '-denoyautees-tramier',
        'nutrilabel': 'A'}
    context = {
        'aliment': aliment
    }
    return render(request, 'main_home/aliment.html', context, {'title': 'Descriptif'})
