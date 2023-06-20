# from django.urls import path
# from . import views

#views
# urlpatterns = [
#     path('<int:pk>', views.IngredientRetrieveAPIView.as_view()),
#     path('', views.IngredientListCreateAPIView.as_view()),
#     path('<int:pk>/update/', views.IngredientUpdateAPIView.as_view()),
#     path('<int:pk>/destroy/', views.IngredientDestroyAPIView.as_view()),
# ]

# viewset
from rest_framework.routers import DefaultRouter
from ingredient.viewsets import IngredientViewSet

router = DefaultRouter()
router.register('', IngredientViewSet, basename='ingredient')

urlpatterns = router.urls
