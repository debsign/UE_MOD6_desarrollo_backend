from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.RecipeRetrieveAPIView.as_view()),
    path('', views.RecipeListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.RecipeUpdateAPIView.as_view()),
    path('<int:pk>/destroy/', views.RecipeDestroyAPIView.as_view()),
]