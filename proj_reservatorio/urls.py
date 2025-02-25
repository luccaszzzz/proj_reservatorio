from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro, perfil, perfil2, gestor, dashboard, detalhe_reservatorio, cadastrar_usuario, listar_usuarios, editar_usuario, remover_usuario # BASEADO NO VÍDEO DE BRUNO - passo 1 - ADICIONEI "cadastrar_usuario" e "listar_usuarios" e "editar_usuario" e "remover_usuario"
from core.views import listar_reservatorios, cadastrar_reservatorio, editar_reservatorio, remover_reservatorio # BASEADO NO VÍDEO DE BRUNO - passo 1 - ADICIONEI "listar_reservatorio", "cadastrar_reservatorio" e "editar_reservatorio"
from core.views import listar_monitoramentos, erro_permissao, cadastrar_monitoramento, editar_monitoramento,remover_monitoramento, my_view, teste# BASEADO NO VÍDEO DE BRUNO - passo 1 - ADICIONEI "listar_monitoramento", "cadastrar_monitoramento" e "editar_monitoramento" e "remover_monitoramento"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('cadastro/', cadastro, name="cadastro"),
    path('perfil/', perfil, name="perfil"),
    path('perfil2/', perfil2, name="perfil2"),
    path('gestor/', gestor, name="gestor"),
    path('dashboard/', dashboard, name="dashboard"),
    path('erro_permissao/', erro_permissao, name="erro_permissao"),

    # CRUD DE USUÁRIOS 
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'), # BASEADO NO VÍDEO DE BRUNO - passo 2 - ADICIONEI a ROTA "cadastrar_usuario"
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'), # BASEADO NO VÍDEO DE BRUNO - passo 2 - CADASTRAR USUARIO - adicionei o "listar_usuarios"
    path('usuario_editar/<int:id>/', editar_usuario, name='editar_usuario'), # BASEADO NO VÍDEO DE BRUNO - passo 3 - EDIÇÃO de usuário
    path('usuario_remover/<int:id>', remover_usuario, name= 'remover_usuario' ),  # BASEADO NO VÍDEO DE BRUNO - passo 4 - REMOÇÃO de usuário

    # CRUD DE RESERVATÓRIO
    path('listar_reservatorios/', listar_reservatorios, name='listar_reservatorios'), # BASEADO NO VÍDEO DE BRUNO - passo 1 - LISTAGEM de RESERVATÓRIO
    path('cadastrar_reservatorio/', cadastrar_reservatorio, name='cadastrar_reservatorio'), # BASEADO NO VÍDEO DE BRUNO - passo 2 - CADASTRO de RESERVATÓRIO
    path('editar_reservatorio/<int:id>/', editar_reservatorio, name='editar_reservatorio'), # BASEADO NO VÍDEO DE BRUNO - passo 3 - EDIÇÃO de RESERVATÓRIO
    path('remover_reservatorio/<int:id>/', remover_reservatorio, name='remover_reservatorio'), # BASEADO NO VÍDEO DE BRUNO - passo 4 - REMOÇÃO de RESERVATÓRIO
    path('detalhe_reservatorio/<int:id>/', detalhe_reservatorio, name='detalhe_reservatorio'), # Define a rota da template de detalhe do reservatorio

    # CRUD DE MONITORAMENTO
    path('listar_monitoramentos/', listar_monitoramentos, name='listar_monitoramentos'), # BASEADO NO VÍDEO DE BRUNO - passo 1 - LISTAGEM de MONITORAMENTO
    path('cadastrar_monitoramento/', cadastrar_monitoramento, name='cadastrar_monitoramento'), # BASEADO NO VÍDEO DE BRUNO - passo 2 - CADASTRO de MONITORAMENTO
    path('editar_monitoramento/<int:id>/', editar_monitoramento, name='editar_monitoramento'), # BASEADO NO VÍDEO DE BRUNO - passo 3 - EDIÇÃO de MONITORAMENTO
    path('remover_monitoramento/<int:id>/', remover_monitoramento, name='remover_monitoramento'), # BASEADO NO VÍDEO DE BRUNO - passo 4 - REMOÇÃO de MONITORAMENTO

    # URLS PARA EXPRESS
    path('messages/', my_view, name='messages'),
    path('teste/', teste, name='teste'),
]