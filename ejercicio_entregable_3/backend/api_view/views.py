from recipe.models import Recipe
from ingredient.models import Ingredient
# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipe.serializer import RecipeSerializer
from ingredient.serializer import IngredientSerializer

@api_view(['GET'])
def api_home(request, *arg, **kargs):
    instance = Recipe.objects.all().order_by('?').first()
    data = {}

    if instance:
        data = RecipeSerializer(instance).data

    return Response(
        data
    )

@api_view(['GET'])
def get_ingredient_recipes(request, *args, **kwargs):
    # Obtener todos los ingredientes
    ingredients = Ingredient.objects.all()
    # Serializar los ingredientes
    ingredient_data = IngredientSerializer(ingredients, many=True).data
    # Obtener todas las recetas
    recipes = Recipe.objects.all()
    # Serializar las recetas
    recipe_data = RecipeSerializer(recipes, many=True).data
    # Crear un diccionario con los datos de ingredientes y recetas
    data = {
        'ingredients': ingredient_data,
        'recipes': recipe_data
    }

    return Response(data)