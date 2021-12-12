from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from . import serializers
from rest_framework import viewsets

from . import models

class FornecedoresView(viewsets.ModelViewSet):
    queryset = models.Fornecedores.objects.all()
    serializer_class = serializers.FornecedoresSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    #método para inserir o campo id_user_cad e registrar o usuário que cadastrou a instância
    def perform_create(self, serializer):
        serializer.save(id_user_cad=self.request.user)

    #método para inserir o campo id_user_alt e registrar o usuário que alterou a instância
    def perform_update(self, serializer):
        serializer.save(id_user_alt=self.request.user)



class Notas_fiscaisView(viewsets.ModelViewSet):
    queryset = models.Notas_fiscais.objects.all()
    serializer_class = serializers.Notas_fiscaisSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    #método para inserir o campo id_user_cad e registrar o usuário que cadastrou a instância
    def perform_create(self, serializer):
        serializer.save(id_user_cad=self.request.user)

    #método para inserir o campo id_user_alt e registrar o usuário que alterou a instância
    def perform_update(self, serializer):
        serializer.save(id_user_alt=self.request.user)

class ItensNotaFiscalView(viewsets.ModelViewSet):
    queryset = models.ItensNotaFiscal.objects.all()
    serializer_class = serializers.ItensNotaFiscalSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    #método para inserir o campo id_user_cad e registrar o usuário que cadastrou a instância
    def perform_create(self, serializer):
        serializer.save(id_user_cad=self.request.user)

    #método para inserir o campo id_user_alt e registrar o usuário que alterou a instância
    def perform_update(self, serializer):
        serializer.save(id_user_alt=self.request.user)

class BensView(viewsets.ModelViewSet):
    queryset = models.Bens.objects.all()
    serializer_class = serializers.BensSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]

    #método para inserir o campo id_user_cad e registrar o usuário que cadastrou a instância
    def perform_create(self, serializer):
        serializer.save(id_user_cad=self.request.user)

    #método para inserir o campo id_user_alt e registrar o usuário que alterou a instância
    def perform_update(self, serializer):
        serializer.save(id_user_alt=self.request.user)

class NaturezasDespesaView(viewsets.ModelViewSet):
    queryset = models.Bens.objects.all()
    serializer_class = serializers.NaturezasDespesaSerializer
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [DjangoModelPermissions]
# Create your views here.