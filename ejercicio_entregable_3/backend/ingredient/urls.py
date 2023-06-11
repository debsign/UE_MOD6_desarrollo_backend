from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.IngredientRetrieveAPIView.as_view()),
    path('', views.IngredientListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.IngredientUpdateAPIView.as_view()),
    path('<int:pk>/destroy/', views.IngredientDestroyAPIView.as_view()),
]