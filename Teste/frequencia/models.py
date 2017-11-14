from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class FaixaHoraria (models.Model):
    nome= models.CharField(max_length= 150, null= True, blank=False)
    horaI = models.TimeField (null = True, blank=False)
    horaF = models.TimeField (null = True, blank=False)
    horaI2 = models.TimeField (blank=True)
    horaF2 = models.TimeField (blank=True)
    def __str__(self):
        return self.nome

class Funcionario (models.Model):
    nome = models.CharField(max_length=300 ,null= True, blank=False)
    chefe = models.CharField(max_length= 300, null= True, blank=False)
    faixaHr = models.ForeignKey(FaixaHoraria, null=True, blank=False)
    def __str__ (self):
        return self.nome

class Frequencia (models.Model):
    dia = models.DateField (null=True, blank=False)
    tipo = models.BooleanField(default=False, verbose_name="Entrada")
    horaRegistro = models.TimeField (null= True, blank=False)
    status = models.BooleanField(default=False, verbose_name="Consistente")
    funcionarios = models.OneToOneField(Funcionario, null=True, blank=False)
    justificativa = models.TextField( blank=True)
    ip = models.IntegerField(null=True, blank=False)
    def __str__ (self):
        return self.dia
