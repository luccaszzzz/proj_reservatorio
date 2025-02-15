from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro, perfil, gestor, usuario_listar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),

    path('login/', login, name="login"),
    path('cadastro/', cadastro, name="cadastro"),
    
    path('perfil/', perfil, name="perfil"),
    path('gestor/', gestor, name="gestor"),

    path('usuario_listar/', usuario_listar, name="usuario_listar"),
]
