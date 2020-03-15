from rest_framework import serializers
from .models import Demanda


class DemandaSerializer(serializers.ModelSerializer):
    anunciante = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Demanda
        fields = (
            'id', 
            'descricao', 
            'cep', 
            'numero', 
            'logradouro', 
            'bairro', 
            'email',
            'telefone',
            'status', 
            'anunciante')