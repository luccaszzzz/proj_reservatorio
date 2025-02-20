# BASEADO NO VÍDEO DE BRUNO - passo 1 - cadastro de usuário
from django.forms import  ModelForm
from .models import Usuario, Reservatorio, Monitoramento
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(ModelForm):
     class Meta:
          model = Usuario
          fields = ['nome', 'email', 'senha', 'cpf','celular']


class ReservatorioForm(ModelForm):
     class Meta:
          model = Reservatorio 
          fields = ['codigo','senha','tempo','periodicidade']

class MonitoramentoForm(ModelForm):
     class Meta:
          model = Monitoramento
          fields = ['data_hora','volume','reservatorio']