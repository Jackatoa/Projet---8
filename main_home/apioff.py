import requests
import re
import json
from unidecode import unidecode
from .food import Food
import ast


class Apioff:
    def get_results_from_search(self, query):
        """ return aliments for a basic query """
        data = self.api_call_results_search(query)
        Food.propositionslst = self.clean_datanewtest(data)
        return Food.propositionslst

    def get_results_from_category(self, categorie, nutriscore):
        """return best aliments with the best category """
        data = self.api_call_results_category(categorie, nutriscore)
        Food.substituteslst = self.clean_data_category(data)
        return Food.substituteslst

    def api_call_results_search(self, query):
        """ simple query call on openfoodfacts api"""
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

    def api_call_results_category(self, category, previousnutri):
        """create query for better nutriscore"""
        dictofbestresulsts = {'products': [], 'count' : 0}
        lstofnutri = ['A', 'B', 'C', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
        id = 0
        while len(dictofbestresulsts['products']) < 6 and id < 6:
            url = "https://world.openfoodfacts.org/cgi/search.pl?"
            nutriscore = lstofnutri[id]
            params = {
                'tagtype_0'     : 'categories',
                'tag_contains_0': 'contains',
                'tag_0'         : category,
                'tagtype_1'     : 'nutrition_grades',
                'tag_contains_1': 'contains',
                'tag_1'         : nutriscore,
                'sort_by'       : 'completeness',
                'page_size'     : '20',
                'axis_x'        : 'energy',
                'axis_y'        : 'product_n',
                'action'        : 'process',
                'json'          : '1',
            }
            response = requests.get(url=url, params=params)
            data = response.json()
            i = 0
            for product in data['products']:
                if 'product_name_fr' in data['products'][i]:
                    if not any(d['product_name_fr'] == data['products'][i]['product_name_fr']
                            for d in dictofbestresulsts['products']):
                        dictofbestresulsts['products'].append(product)
                        dictofbestresulsts['count'] += 1
                i += 1
            id += 1
        return dictofbestresulsts

    def select_categorie(self, data):
        """return the best category"""
        referencenumber = 1000000
        finalcategory = ''
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
        i = 0
        newlstdata = []
        while i < len(data):
            if data[i] != '':
                newlstdata.append(data[i])
            i += 1
        for category in newlstdata:
            if category not in lstofuselesscategory:
                url = "https://world.openfoodfacts.org/category/" + category + ".json"
                response = requests.get(url)
                newdata = response.json()
                if newdata['count'] < referencenumber:
                    referencenumber = newdata['count']
                    finalcategory = category
        return finalcategory

    def get_aliment_dict(self, data, aliment, i):
        """return cleaned aliment"""
        if 'product_name_it' in data['products'][i]:
            if data['products'][i]['product_name_it'] is not '':
                aliment['product_name_fr'] = data['products'][i]['product_name_it']
        if 'product_name_en' in data['products'][i]:
            if data['products'][i]['product_name_en'] is not '':
                aliment['product_name_fr'] = data['products'][i]['product_name_en']
        if 'product_name' in data['products'][i]:
            if data['products'][i]['product_name'] is not '':
                aliment['product_name_fr'] = data['products'][i]['product_name']
        if 'product_name_fr' in data['products'][i]:
            if data['products'][i]['product_name_fr'] is not '':
                aliment['product_name_fr'] = data['products'][i]['product_name_fr']
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
        aliment['url'] = "https://fr.openfoodfacts.org/produit/" + aliment['code']
        aliment['info'].append(aliment['categorie'])
        aliment['info'].append(aliment['nutriletter'])
        return aliment

    def get_aliment_dict_hard(self, data, aliment, i):
        """return only full documented aliments"""
        if all(name in data['products'][i].keys() for name in ('product_name_fr', 'image_url',
                                                               'image_nutrition_url',
                                                               'nutrition_grades', 'id',
                                                               'categories_tags', 'stores_tags')):
            aliment['product_name_fr'] = data['products'][i]['product_name_fr']
            aliment['img'] = data['products'][i]['image_url']
            aliment['url_nutri'] = data['products'][i]['image_nutrition_url']
            aliment['nutriletter'] = data['products'][i]['nutrition_grades'].upper()
            aliment['code'] = data['products'][i]['id']
            aliment['categorie'] = data['products'][i]['categories_tags']
            if data['products'][i]['stores_tags'] != '':
                aliment['stores'] = data['products'][i]['stores_tags']
            aliment['nutriscore'] += aliment['nutriletter'].lower()
            aliment['url'] = "https://fr.openfoodfacts.org/produit/" + aliment['code']
            aliment['info'].append(aliment['categorie'])
            aliment['info'].append(aliment['nutriletter'])
            return aliment

    def clean_datanewtest(self, data):
        """return the best aliments by checking completness and already entred aliments"""
        newdata = []
        i = 0
        fulltry = True
        nutry = True
        nametry = True
        finaltry = True
        if data['count'] < 20:
            maxresult = data['count']
        else:
            maxresult = 20

        while len(newdata) <= 5 and finaltry is not False:
            aliment = {'product_name_fr': 'default name',
                       'img'            : 'default img', 'nutriscore': 'nutri', 'nutriletter': '?',
                       'code'           : '0', 'url_nutri': 'default nutriimg',
                       'categorie'      : 'en:cocoa-and-hazelnuts-spreads', 'info': [], 'stores'
                       : 'no stores'}

            if i == maxresult and fulltry:
                i = 0
                fulltry = False
            elif i == maxresult and nutry:
                i = 0
                nutry = False
            elif i == maxresult and nametry:
                i = 0
                nametry = False
            elif i == maxresult and finaltry:
                i = 0
                finaltry = False

            if not newdata:
                if fulltry:
                    result = a.get_aliment_dict_hard(data, aliment, i)
                    if result is not None:
                        newdata.append(result)
                    i += 1
                elif nametry:
                    if 'product_name_fr' in data['products'][i]:
                        result = a.get_aliment_dict_hard(data, aliment, i)
                        if result is not None:
                            newdata.append(result)
                    i += 1
                elif finaltry:
                    if 'product_name_it' in data['products'][i] or 'product_name_en' in data[
                        'products'][i] or 'product_name' in data['products'][i]:
                        newdata.append(a.get_aliment_dict(data, aliment, i))
                    i += 1
            else:
                if fulltry:
                    if 'product_name_fr' in data['products'][i]:
                        if data['products'][i]['product_name_fr'] is not '':
                            if not any(
                                    d['product_name_fr'] == data['products'][i]['product_name_fr']
                                    for d in newdata):
                                result = a.get_aliment_dict_hard(data, aliment, i)
                                if result is not None:
                                    newdata.append(result)
                    i += 1
                elif nametry:
                    if 'product_name_fr' in data['products'][i]:
                        if data['products'][i]['product_name_fr'] is not '':
                            result = a.get_aliment_dict_hard(data, aliment, i)
                            if result is not None:
                                newdata.append(result)
                    i += 1
                elif finaltry:
                    if 'product_name_it' in data['products'][i] or 'product_name_en' in data[
                        'products'][i] or 'product_name' in data['products'][i]:
                        result = a.get_aliment_dict(data, aliment, i)
                        if result is not None:
                            newdata.append(result)
                    i += 1
        return newdata

    def clean_data_category(self, data):
        """return a cleaned aliment"""
        newdata = []
        i = 0
        if len(data['products']) < 6 :
            maxresult = len(data['products'])
        else:
            maxresult = 5
        while len(newdata) <= maxresult - 1:
            aliment = {'product_name_fr': 'default name',
                       'img'            : 'default img', 'nutriscore': 'nutri', 'nutriletter': '?',
                       'code'           : '0', 'url_nutri': 'default nutriimg',
                       'categorie'      : 'en:cocoa-and-hazelnuts-spreads', 'info': [], 'stores'
                       : 'no stores'}
            newdata.append(a.get_aliment_dict(data, aliment, i))
            i += 1
        return newdata


f = Food('', '', '', '', '', '', '')
a = Apioff()
