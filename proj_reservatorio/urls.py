from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro, perfil, gestor, usuario_listar, reservatorio_listar, monitoramento_listar, dashboard, detalhe_reservatorio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),

    path('login/', login, name="login"),
    path('cadastro/', cadastro, name="cadastro"),
    
    path('perfil/', perfil, name="perfil"),
    path('gestor/', gestor, name="gestor"),

    path('usuario_listar/', usuario_listar, name="usuario_listar"),
    path('reservatorio_listar/', reservatorio_listar, name="reservatorio_listar"),
    path('monitoramento_listar/', monitoramento_listar, name="monitoramento_listar"),

    path('dashboard/', dashboard, name="dashboard"),
    path('detalhe_reservatorio/', detalhe_reservatorio, name="detalhe_reservatorio"),
]
