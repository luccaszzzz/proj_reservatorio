from django.db import models 
from django.contrib.auth.models import User 
# POSSÍVEL SOLUÇÃO DO PROBLEMA DE CADASTRO DE RESERVATÓRIO


class Usuario(models.Model):  

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    # POSSÍVEL SOLUÇÃO DO PROBLEMA DE CADASTRO DE RESERVATÓRIO

    nome = models.CharField(max_length=100)  
    email = models.EmailField(unique=True)  
    senha = models.CharField(max_length=128)  
    cpf = models.CharField(max_length=11, unique=True)  
    celular = models.CharField(max_length=15) 

    def __str__(self):    
        return self.user.username
    # POSSÍVEL SOLUÇÃO DO PROBLEMA DE CADASTRO DE RESERVATÓRIO
    '''
    def __str__(self):    
        return self.nome  # Retorna o nome do usuário como representação do objeto
    '''
class Reservatorio(models.Model):   
    codigo = models.CharField(max_length=50, unique=True)  
    senha = models.CharField(max_length=128)  
    tempo = models.IntegerField()  
    
    # Periodicidade do reservatório, com opções limitadas para garantir validade dos dados  
    periodicidade = models.CharField(max_length=50, choices=[  
        ('semanal', 'Semanal'),  
        ('mensal', 'Mensal'),  
        ('diario', 'Diário'),  
    ])  
    
    # Relacionamento com o modelo Usuario, definindo que cada reservatório pertence a um usuário  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True, blank=True)  

    def __str__(self):  
        return self.codigo  


class Monitoramento(models.Model):   
    data_hora = models.DateTimeField()  
    volume = models.FloatField()   
    reservatorio = models.ForeignKey(Reservatorio, on_delete=models.CASCADE)  

    def __str__(self):  
        return f"Monitoramento em {self.data_hora} - Volume: {self.volume}"