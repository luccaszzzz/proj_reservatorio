from django.contrib import admin
from .models import Usuario, Reservatorio, Monitoramento

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'celular')
    search_fields = ('nome', 'email', 'cpf')

@admin.register(Reservatorio)
class ReservatorioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'usuario', 'tempo', 'periodicidade')
    search_fields = ('codigo',)
    list_filter = ('usuario', 'periodicidade')

@admin.register(Monitoramento)
class MonitoramentoAdmin(admin.ModelAdmin):
    list_display = ('reservatorio', 'data_hora', 'volume')
    list_filter = ('reservatorio', 'data_hora')
    ordering = ('-data_hora',)