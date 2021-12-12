from rest_framework import serializers

from . import models

class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fornecedores
        fields = '__all__'

class Notas_fiscaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notas_fiscais
        fields = '__all__'

class ItensNotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItensNotaFiscal
        fields = '__all__'

class BensSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bens
        fields = '__all__'

class NaturezasDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NaturezasDespesa
        fields = '__all__'

