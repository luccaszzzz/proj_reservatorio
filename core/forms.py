# BASEADO NO VÍDEO DE BRUNO - passo 1 - cadastro de usuário
from django.forms import  ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):
     class Meta:
          model = Usuario
          fields = ['nome', 'email', 'senha', 'cpf','celular']

          