from django.shortcuts import render
from .models import Recipe
from .serializer import RecipeSerializer

from rest_framework import generics


class RecipeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeUpdateAPIView(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    def perform_update(self, serializer):
        instance = serializer.save()

class RecipeDestroyAPIView(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
