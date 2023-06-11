from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('ingredient-recipes/', views.get_ingredient_recipes)
]