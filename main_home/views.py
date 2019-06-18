from django.shortcuts import render, redirect
from .models import AlimentSaved, Aliment
from .apioff import Apioff
import ast
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'main_home/home.html')

@login_required
def saved(request):
    als = AlimentSaved.objects.filter(author=request.user)
    context = {
        'aliment_saveds': als
    }
    return render(request, 'main_home/saved.html', context)

def search(request):
    if request.method == 'POST':
        if "next" in request.POST:
            value = {}
            value['next'] = request.POST.get('next', None)
            finalvalue = ast.literal_eval(value['next'])
            categorie = a.select_categorie(finalvalue['info'][0])
            context = {'foods': a.get_results_from_category(categorie, finalvalue['info'][1]),
                       'firstfood': value['next']}
            return render(request, 'main_home/search.html', context, {'title': 'Descriptif'})
    return render(request, 'main_home/search.html', {'title': 'Résultats'})

@login_required
def confirmation(request):
    if request.method == 'POST':
        if "save" in request.POST:
            value = {}
            value['save'] = request.POST.get('save', None)
            finalvalue = ast.literal_eval(value['save'])
            newaliment1 = Aliment(
                name=finalvalue[0]['product_name_fr'],
                url=finalvalue[0]['url'],
                url_img=finalvalue[0]['img'],
                url_nutri=finalvalue[0]['url_nutri'],
                category=finalvalue[0]['categorie'],
                stores=finalvalue[0]['stores'],
                nutriscore=finalvalue[0]['nutriletter'])

            newaliment2 = Aliment(
                name=finalvalue[1]['product_name_fr'],
                url=finalvalue[1]['url'],
                url_img=finalvalue[1]['img'],
                url_nutri=finalvalue[1]['url_nutri'],
                category=finalvalue[1]['categorie'],
                stores=finalvalue[1]['stores'],
                nutriscore=finalvalue[1]['nutriletter'])

            newaliment1.save()
            newaliment2.save()
            alimentsaved = AlimentSaved(
                urloriginal= Aliment.objects.get(url=finalvalue[0]['url']),
                urlsubstitute= Aliment.objects.get(url=finalvalue[1]['url']),
                author=request.user)
            alimentsaved.save()

            messages.success(request, f'Vos choix ont bien été enregistrés !')
            return redirect('../')

def aliment(request):
    value = {}
    value['info'] = request.POST.get('info', None)
    context = {
        'aliment': ast.literal_eval(value['info'])}
    return render(request, 'main_home/aliment.html', context, {'title': 'Descriptif'})

def infosaved(request):
    value = {}
    value['info'] = request.POST.get('info', None)
    al = Aliment.objects.get(url=value['info'])
    context = {
        'aliment': al
    }
    return render(request, 'main_home/infosaved.html', context, {'title': 'Descriptif'})

def proposition(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            context = {'foods': a.get_results_from_search(query)}
            return render(request, 'main_home/proposition.html', context, {'title': 'Proposition'})

@login_required
def delete(request):
    if request.method == 'POST':
        if "delete" in request.POST:
            value = {}
            value['delete'] = request.POST.get('delete', None)
            context = {
                'aliment': value['delete']
            }
            return render(request, 'main_home/delete.html', context, {'title': 'Suppression'})

def validatedelete(request):
    if request.method == 'POST':
        if "delete" in request.POST:
            value = {}
            value['delete'] = request.POST.get('delete', None)
            al = Aliment.objects.get(url=value['delete'])
            al.delete()
            messages.success(request, f'Aliments supprimés !')
            return redirect('../')

a = Apioff()
