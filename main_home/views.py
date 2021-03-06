from django.shortcuts import render, redirect, get_object_or_404
from .models import AlimentSaved, Aliment
from .apioff import Apioff
import ast
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import re

# Create your views here.
def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def home(request):
    return render(request, 'main_home/home.html')


@login_required
def saved(request):
    als = AlimentSaved.objects.filter(author=request.user)
    paginator = Paginator(als, 10)
    page = request.GET.get('page')
    aliments = paginator.get_page(page)
    context = {
        'aliment_saveds': als, 'aliments': aliments
    }
    return render(request, 'main_home/saved.html', context)

class SavedListView(LoginRequiredMixin,ListView):
    model = AlimentSaved
    template_name = 'main_home/saved.html'
    context_object_name = 'aliment_saveds'
    paginate_by = 4

    def get_queryset(self):
        return AlimentSaved.objects.filter(author=self.request.user)

def search(request):
    if request.method == 'POST':
        if "next" in request.POST:
            value = {}
            value['next'] = request.POST.get('next', None)
            finalvalue = ast.literal_eval(value['next'])
            categorie = a.select_categorie(finalvalue['info'][0])
            context = {'foods'    : a.get_results_from_category(categorie, finalvalue['info'][1]),
                       'firstfood': value['next']}
            return render(request, 'main_home/search.html', context, {'title': 'Descriptif'})
    return render(request, 'main_home/search.html', {'title': 'Résultats'})

def searchnova(request):
    if request.method == 'POST':
        if "next" in request.POST:
            value = {}
            value['next'] = request.POST.get('next', None)
            finalvalue = ast.literal_eval(value['next'])
            categorie = a.select_categorie(finalvalue['info'][0])
            context = {'foods'    : a.get_results_from_category_nova(categorie, finalvalue['info'][
                1]),
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
                nutriscore=finalvalue[0]['nutriletter'],
                novascore=finalvalue[0]['novascore'],
                author=request.user)

            newaliment2 = Aliment(
                name=finalvalue[1]['product_name_fr'],
                url=finalvalue[1]['url'],
                url_img=finalvalue[1]['img'],
                url_nutri=finalvalue[1]['url_nutri'],
                category=finalvalue[1]['categorie'],
                stores=finalvalue[1]['stores'],
                nutriscore=finalvalue[1]['nutriletter'],
                novascore=finalvalue[1]['novascore'],
                author=request.user)

            newaliment1.save()
            newaliment2.save()
            alimentsaved = AlimentSaved(
                urloriginal=Aliment.objects.filter(url=finalvalue[0]['url'])[0],
                urlsubstitute=Aliment.objects.filter(url=finalvalue[1]['url'])[0],
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
    al = Aliment.objects.filter(url=value['info']).first()
    context = {
        'aliment': al, 'stores': ast.literal_eval(al.stores)
    }
    return render(request, 'main_home/infosaved.html', context, {'title': 'Descriptif'})


def proposition(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            if re.search('[a-zA-Z]', query):
                results = a.get_results_from_search(query)
                print(results)
                if results:
                    context = {'foods': results}
                    return render(request, 'main_home/proposition.html', context,
                                  {'title': 'Proposition'})
                else:
                    context = {'message': 'noresults'}
                    return render(request, 'main_home/home.html', context)
            else:
                context = {'message': 'noresults'}
                return render(request, 'main_home/home.html', context)

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
            id = int(value['delete'])
            al = AlimentSaved.objects.get(id=id)
            al.delete()
            messages.success(request, f'Aliments supprimés !')
            return redirect('../saved/')

class AlimentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AlimentSaved
    success_url = '/saved/'

    def test_func(self):
        alimentsaved = self.get_object()
        if self.request.user == alimentsaved.author:
            return True
        return False

def mention(request):
    return render(request, 'main_home/mention.html', {'title': 'Mentions légales'})


a = Apioff()
