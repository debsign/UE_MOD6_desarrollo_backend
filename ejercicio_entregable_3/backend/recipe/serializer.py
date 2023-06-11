from rest_framework import serializers
from ingredient.serializer import IngredientSerializer

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'title',
            'steps',
            'ingredients',
        ]
