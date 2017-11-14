from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from frequencia.serializers import *
# Create your views here.
class FaixaHorariaViewSet (viewsets.ModelViewSet):
    queryset = FaixaHoraria.objects.all()
    serializer_class = FaixaHorariaSerializer

class FuncionarioViewSet (viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FrequenciaViewSet (viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer
