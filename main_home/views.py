from django.shortcuts import render, redirect
from .models import Aliment
from .apioff import Apioff
import ast

# Create your views here.

def home(request):
    return render(request, 'main_home/home.html')


def saved(request):
    return render(request, 'main_home/saved.html')


def search(request):
    if request.method == 'POST':
        if "next" in request.POST:
            value = {}
            value['next'] = request.POST.get('next', None)
            finalvalue = ast.literal_eval(value['next'])
            categorie = a.select_categorie(finalvalue[0])
            context = {'foods': a.get_results_from_category(categorie, finalvalue[1])}
            return render(request, 'main_home/search.html', context, {'title': 'Descriptif'})
    return render(request, 'main_home/search.html', {'title': 'Résultats'})


def aliment(request):
    value = {}
    value['info'] = request.POST.get('info', None)
    context = {
        'aliment': ast.literal_eval(value['info'])}
    return render(request, 'main_home/aliment.html', context, {'title': 'Descriptif'})


def proposition(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            context = {'foods': a.get_results_from_search(query)}
            return render(request, 'main_home/proposition.html', context, {'title': 'Proposition'})

a = Apioff()
