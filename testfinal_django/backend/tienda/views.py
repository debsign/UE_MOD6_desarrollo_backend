from rest_framework import viewsets
from .serializers import TiendaSerializer
from .models import Tienda

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer
