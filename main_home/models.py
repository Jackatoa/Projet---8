from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Aliment(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    url_img = models.TextField()
    url_nutri = models.TextField()
    category = models.TextField()
    stores = models.TextField()
    nutriscore = models.CharField(max_length=1)

    def __str__(self):
        return self.name



class AlimentSaved(models.Model):
    urloriginal = models.ForeignKey('Aliment', on_delete=models.CASCADE,
                                    related_name='originals')
    urlsubstitute = models.ForeignKey('Aliment', on_delete=models.CASCADE,
                                    related_name='substituted')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.urlsubstitute.name
