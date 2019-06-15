import requests
import re
import json
from unidecode import unidecode
from .food import Food
import ast


class Apioff:
    def get_results_from_search(self, query):
        data = self.api_call_results_search(query)
        Food.propositionslst = self.clean_data(data)
        return Food.propositionslst

    def get_results_from_category(self, category):
        data = self.api_call_results_category(category)
        Food.substituteslst = self.clean_data(data)
        return Food.substituteslst

    def api_call_results_search(self, query):
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

    def api_call_results_category(self, category):
        url = "https://fr.openfoodfacts.org/categorie/" + category + ".json"
        response = requests.get(url=url)
        data = response.json()
        return data

    def clean_data(self, data):
        newdata = []
        i = 0
        while i <= 39 and len(newdata) <= 5:
            aliment = {'name'     : 'default name',
                       'img'      : 'default img', 'nutriscore': 'nutri', 'nutriletter': '?',
                       'code'     : '0', 'url_nutri': 'default nutriimg',
                       'categorie': 'en:cocoa-and-hazelnuts-spreads'}
            if newdata:
                if not any(d['name'] == data['products'][i]['product_name_fr'] for d in newdata):
                    if i >= 20 and len(newdata) < 5:
                        newdata.append(a.get_aliment_dict(data, aliment, i))
                        i += 1
                    elif i <= 19 and len(newdata) <= 5:
                        newdata.append(a.get_aliment_dict_hard(data, aliment, i))
                        i += 1
                    else:
                        print("ca naurait pas du arrivé2")
                else:
                    i += 1
            else:
                if i >= 20 and len(newdata) < 5:
                    newdata.append(a.get_aliment_dict(data, aliment, i))
                    i += 1
                elif i <= 19 and len(newdata) <= 5:
                    newdata.append(a.get_aliment_dict_hard(data, aliment, i))
                    i += 1
                else:
                    print("ca naurait pas du arrivé")
        return newdata

    def select_categorie(self, data):
        print('select categorie')
        referencenumber = 1000000
        finalcategory = ''
        data = ast.literal_eval(data)
        print(data[0])
        lstofuselesscategory = ["en:plant-based-foods-and-beverages", "en:plant-based-foods",
                                "en:snacks", "en:beverages", "en:sweet-snacks", "en:dairies",
                                "en:meats", "en:non-alcoholic-beverages", "en:meals",
                                "en:fruits-and-vegetables-based-foods",
                                "en:cereals-and-potatoes", "en:fermented-foods",
                                "en:fermented-milk-products", "en:spreads", "en:biscuits-and-cakes",
                                "en:groceries", "en:prepared-meats",
                                "en:cereals-and-their-products", "en:cheeses", "en:breakfasts",
                                "en:plant-based-beverages", "en:fruits-based-foods", "en:desserts",
                                "en:sauces", "en:sweet-spreads", "en:frozen-foods",
                                "en:canned-foods", "en:vegetables-based-foods", "en:seafood",
                                "en:confectioneries", "en:alcoholic-beverages",
                                "en:plant-based-spreads", "en:biscuits", "en:fruit-based-beverages",
                                "en:chocolates", "en:fishes", "en:salty-snacks", "en:fats",
                                "en:juices-and-nectars", "en:sweetened-beverages", "en:condiments",
                                "en:meat-based-products", "en:yogurts", "en:cakes",
                                "en:fruit-juices-and-nectars", "en:french-cheeses",
                                "en:fresh-foods", "en:poultries", "en:appetizers",
                                "en:fruit-preserves", "en:breads", "en:dried-products",
                                "en:fruit-juices", "en:jams", "en:meals-with-meat",
                                "en:cow-cheeses", "en:legumes-and-their-products",
                                "en:canned-plant-based-foods", "en:salted-spreads",
                                "en:unsweetened-beverages", "en:sweeteners",
                                "en:nuts-and-their-products", "en:fruit-jams", "en:seeds",
                                "en:hot-beverages", "en:chickens", "en:farming-products",
                                "en:vegetable-fats", "en:pastas", "en:wines",
                                "en:breakfast-cereals", "en:milks", "en:hams", "en:legumes",
                                "en:vegetable-oils", "en:chips-and-fries", "en:carbonated-drinks"]
        for category in data:
            if category not in lstofuselesscategory:
                url = "https://world.openfoodfacts.org/category/" + category + ".json"
                response = requests.get(url)
                newdata = response.json()
                if newdata['count'] < referencenumber:
                    referencenumber = newdata['count']
                    finalcategory = category
        print(referencenumber)
        print(finalcategory)
        return finalcategory

    def get_aliment_dict(self, data, aliment, i):
        if 'product_name_fr' in data['products'][i]:
            aliment['name'] = data['products'][i]['product_name_fr']
        if 'image_url' in data['products'][i]:
            aliment['img'] = data['products'][i]['image_url']
        if 'image_nutrition_url' in data['products'][i]:
            aliment['url_nutri'] = data['products'][i]['image_nutrition_url']
        if 'nutrition_grades' in data['products'][i]:
            aliment['nutriletter'] = data['products'][i]['nutrition_grades'].upper()
        if 'id' in data['products'][i]:
            aliment['code'] = data['products'][i]['id']
        if 'categories_tags' in data['products'][i]:
            aliment['categorie'] = data['products'][i]['categories_tags']
        if 'stores_tags' in data['products'][i]:
            aliment['stores'] = data['products'][i]['stores_tags']
        aliment['nutriscore'] += aliment['nutriletter'].lower()
        return aliment

    def get_aliment_dict_hard(self, data, aliment, i):
        if all(name in data['products'][i].keys() for name in ('product_name_fr', 'image_url',
                                                               'image_nutrition_url',
                                                               'nutrition_grades', 'id',
                                                               'categories_tags', 'stores_tags')):
            aliment['name'] = data['products'][i]['product_name_fr']
            aliment['img'] = data['products'][i]['image_url']
            aliment['url_nutri'] = data['products'][i]['image_nutrition_url']
            aliment['nutriletter'] = data['products'][i]['nutrition_grades'].upper()
            aliment['code'] = data['products'][i]['id']
            aliment['categorie'] = data['products'][i]['categories_tags']
            aliment['stores'] = data['products'][i]['stores_tags']
            aliment['nutriscore'] += aliment['nutriletter'].lower()
            return aliment

    def
f = Food('', '', '', '', '', '', '')
a = Apioff()
