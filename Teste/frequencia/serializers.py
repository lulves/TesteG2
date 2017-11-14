from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from frequencia.views import FaixaHoraria, Funcionario, Frequencia

class FaixaHorariaSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FaixaHoraria
        fields = ('nome','horaI', 'horaF', 'horaI2', 'horaF2')

class FuncionarioSerializer (serializers.HyperlinkedModelSerializer):
    #faixaHr = FaixaHorariaSerializer(many='False')
    class Meta:
        model = Funcionario
        fields = ('nome', 'chefe', 'faixaHr')

class FrequenciaSerializer (serializers.HyperlinkedModelSerializer):
    #funcionarios = FuncionarioSerializer(many='False')
    class Meta:
        model = Frequencia
        fields = ('dia', 'tipo','horaRegistro','status', 'funcionarios', 'justificativa', 'ip')
