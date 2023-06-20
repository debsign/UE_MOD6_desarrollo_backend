from django.shortcuts import render
from .models import Ingredient
from .serializer import IngredientSerializer

from rest_framework import generics

class IngredientRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientUpdateAPIView(generics.UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    def perform_update(self, serializer):
        instance = serializer.save()

class IngredientDestroyAPIView(generics.DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
