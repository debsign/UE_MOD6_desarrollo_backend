from rest_framework.routers import DefaultRouter
from ingredient.viewsets import IngredientViewSet

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredient')

urlpatterns = router.urls