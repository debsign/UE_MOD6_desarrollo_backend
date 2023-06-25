from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TiendaViewSet

router = DefaultRouter()

router.register('', TiendaViewSet, basename='tienda')

urlpatterns = router.urls