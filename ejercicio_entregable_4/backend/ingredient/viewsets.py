from rest_framework import viewsets

from .models import Ingredient
from .serializer import IngredientSerializer

# bastante similar a lo que teníamos en el genérico
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'pk'