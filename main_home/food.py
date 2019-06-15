class Food:
    propositionslst = []
    substituteslst = []

    def __init__(self, name, img, nutriimg, nutriletter, code, category, nutriscore):
        self.name = name
        self.img = img
        self.nutriimg = nutriimg
        self.nutriletter = nutriletter
        self.code = code
        self.url = "https://fr.openfoodfacts.org/produit/" + self.code
        self.apiurl = "https://fr.openfoodfacts.org/api/v0/produit/" + self.code
        self.category = category
        self.nutriscore = nutriscore

    def create_list(self, lst):
        newlist = []
        for aliment in lst:
            newfood = Food(aliment['name'], aliment['img'], aliment['url_nutri'],
                           aliment['nutriletter'], aliment['code'], aliment['categorie'],
                           aliment['nutriscore'])
            newlist.append(newfood)
            return newlist


