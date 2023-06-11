from django.db import models
from ingredient.models import Ingredient

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    steps = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)