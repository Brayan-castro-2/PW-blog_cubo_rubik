from dataclasses import field
from rest_framework import serializers
from app1.models import patrones

class patronesSerializers(serializers.ModelSerializer):
    class Meta:
        model= patrones
        fields=['id','usuario','categoria','seccion','algoritmo','comentarios']
