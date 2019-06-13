import requests
import re
import json

def get_results(query):
    data = api_call(query)
    data = clean_data(data)
    data = get_nutriscore(data)
    return data

def api_call(query):
    url = "https://fr.openfoodfacts.org/cgi/search.pl?"
    params = {
        'action'       : 'process',
        'search_terms' : query,
        'search_simple': 1,
        'json'         : 1,
    }
    response = requests.get(url=url, params=params)
    data = response.json()
    return data

def clean_data(data):
    newdata = []
    i = 0
    print(len(data['products']))
    if len(data['products']) >= 6:
        id = 5
    else:
        id = len(data['products']) - 1
    while i <= id:
        aliment = {'name': 'default name',
                   'img' : 'default img', 'nutriscore': 'nutri', 'nutriletter': '?'}
        if 'product_name_fr' in data['products'][i].keys():
            aliment['name'] = data['products'][i]['product_name_fr']
            if 'image_url' in data['products'][i].keys():
                aliment['img'] = data['products'][i]['image_url']
            if 'nutrition_grades' in data['products'][i].keys():
                aliment['nutriletter'] = data['products'][i]['nutrition_grades'].upper()
        else:
            id += 1
        newdata.append(aliment)
        i += 1
    return newdata

def get_nutriscore(data):
    for aliment in data:
        aliment['nutriscore'] += aliment['nutriletter'].lower()
    return data
