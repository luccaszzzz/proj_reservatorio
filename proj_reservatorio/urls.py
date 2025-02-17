from django.contrib import admin
from django.urls import path, include
from core.views import (
    home,
    login,
    cadastro,
    perfil,
    gestor,
    usuario_listar2,
    reservatorio_listar,
    monitoramento_listar,
    dashboard,
    detalhe_reservatorio,
    cadastrar_usuario,
    listar_usuarios,
    editar_usuario,
    remover_usuario,
)  # BASEADO NO VÍDEO DE BRUNO - passo 1 - ADICIONEI "cadastrar_usuario" e "listar_usuarios" e "editar_usuario" e "remover_usuario"
from core.views import (
    listar_reservatorio,
)  # BASEADO NO VÍDEO DE BRUNO - passo 1 - ADICIONEI "listar_reservatorio"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path(
        "cadastrar_usuario/", cadastrar_usuario, name="cadastrar_usuario"
    ),  # BASEADO NO VÍDEO DE BRUNO - passo 2 - ADICIONEI a ROTA "cadastrar_usuario"
    path(
        "listar_usuarios/", listar_usuarios, name="listar_usuarios"
    ),  # BASEADO NO VÍDEO DE BRUNO - passo 2 - CADASTRAR USUARIO - adicionei o "listar_usuarios"
    path(
        "usuario_editar/<int:id>/", editar_usuario, name="editar_usuario"
    ),  # BASEADO NO VÍDEO DE BRUNO - passo 3 - EDIÇÃO de usuário
    path(
        "usuario_remover/<int:id>", remover_usuario, name="remover_usuario"
    ),  # BASEADO NO VÍDEO DE BRUNO - passo 4 - REMOÇÃO de usuário
    path(
        "listar_reservatorio/", listar_reservatorio, name="listar_reservatorio"
    ),  # BASEADO NO VÍDEO DE BRUNO - passo 1 - LISTAGEM de RESERVATÓRIO
    path("login/", login, name="login"),
    path("cadastro/", cadastro, name="cadastro"),
    path('autenticacao/', include('autenticacao.urls')), # 
    path("perfil/", perfil, name="perfil"),
    path("gestor/", gestor, name="gestor"),
    path("usuario_listar2/", usuario_listar2, name="usuario_listar2"),
    path("reservatorio_listar/", reservatorio_listar, name="reservatorio_listar"),
    path("monitoramento_listar/", monitoramento_listar, name="monitoramento_listar"),
    path("dashboard/", dashboard, name="dashboard"),
    path("detalhe_reservatorio/", detalhe_reservatorio, name="detalhe_reservatorio"),
]
