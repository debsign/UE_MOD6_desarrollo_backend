from rest_framework import serializers
from .models import Tienda

class TiendaSerializer(serializers.ModelSerializer):
    dias_abierta = serializers.SerializerMethodField()

    class Meta:
        model = Tienda
        fields = '__all__'

    def get_dias_abierta(self, obj):
        return obj.dias_abierta

    def validate_ciudad(self, value):
        # comprueba que la ciudad es Madrid
        if value.lower() != 'madrid':
            raise serializers.ValidationError("La tienda debe estar en Madrid.")
        return value