# Pur Beurre

Cette application web propose à l'utilisateur des alternatives alimentaires en fonction du nutri-score depuis l'API d'OpenFoodFacts.org. L'utilisateur peut créer un compte et enregistrer ses choix par la même occasion.

### Prérequis

Tout les dépendances sont dans le fichier requirements.txt.

```
$ pip install -r requirements.txt
```

### Utilisation

Vous pouvez utiliser Pur Beurre ici : https://breadandpurebutter.herokuapp.com

Pur Beurre propose un formulaire de recherche, tapez y un aliment et il vous proposera 6 aliments dont le nom est similaire, vous pouvez ensuite soit obtenir des informations sur ces aliments soit en sélectionner un, vous aurez alors des propositions basés sur la catégorie de cet aliment. Si vous créez un compte, vous pouvez aussi enregistrer vos choix et les retrouver facilement.

```
Nutella
```

Retournera plusieurs types de produit à base de Nutella. 

Après sélection d'un produit différentes types de pâtes à tartiner au chocolat et aux noisettes avec un bien meilleur nutri-score apparaitrons.

## Créé avec

* [DJANGO](https://www.djangoproject.com) - The web framework for perfectionists with deadlines.
* [OpenFoodFacts.org](https://world.openfoodfacts.org) - Open Food Facts is a food products database made by everyone, for everyone.

## Auteur

* **Xavier Endres** 



