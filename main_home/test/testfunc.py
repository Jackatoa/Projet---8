import unittest
from main_home.apioff import Apioff

class BotTests(unittest.TestCase):

    def test_select_categorie(self):
        data = ["en:cocoa-and-hazelnuts-spreads", "en:fruit-juices"]
        element = a.select_categorie(data)
        assert element == "en:cocoa-and-hazelnuts-spreads"

    def test_select_categorie_fail(self):
        data = ["en:cocoa-and-hazelnuts-spreads", "en:fruit-juices"]
        element = a.select_categorie(data)
        assert element != "en:fruit-juices"

    def test_call_results_search_succes(self):
        element = a.api_call_results_search("nutella")
        assert element['products']

    def test_call_results_search_fail(self):
        element = a.api_call_results_search("qsfsghjdfv")
        assert not element['products']



a = Apioff()
