from django.db import models

# Create your models here.
class Favoritos(models.Model):
    name = models.CharField(max_length=50, blank=True)
    url = models.URLField()