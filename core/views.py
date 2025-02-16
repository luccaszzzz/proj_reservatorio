from django.shortcuts import render, redirect #adicionado dia 13/02 pela vídeo aula de Bruno passo 2 CADASTRAR USUÁRIO
from .models import Usuario #adicionado dia 13/02 pela vídeo aula de Bruno passo 1 LOGIN REGISTRAR USUÁRIO
from  .forms import UsuarioForm #adicionado dia 13/02 pela vídeo aula de Bruno passo 2 CADASTRAR USUÁRIO
from .models import Reservatorio #adicionado dia 14/02 pela vídeo aula de Bruno passo 1 LISTAGEM DE RESERVATÓRIO

# não sei se isto está certo - passo 2 de Bruno -  LOGIN REGISTRAR USUÁRIO - 13/02
# o código abaixo foi preenchido automaticamente - 13/02 - passo 2 de Bruno
#def registrar_usuario(request):
   # if request.method == 'POST':
    #    nome = request.POST.get('nome')
     #   email = request.POST.get('email')
      #  senha = request.POST.get('senha')
       # cpf = request.POST.get('cpf')
        #celular = request.POST.get('celular')
        #usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf, celular=celular)
        #usuario.save()
    #return render(request, 'cadastro.html')


# BASEADO NO VÍDEO DE BRUNO - passo 1 -LISTAGEM de usuário
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {
        'listagem_usuarios': usuarios
    }
    return render(request, 'usuarios/listagem_usuarios.html', contexto)
    
# BASEADO NO VÍDEO DE BRUNO - passo 2 - CADASTRO de usuário
def cadastrar_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios')
    contexto = {
        'form_usuario': form
    }
    return render(request, 'usuarios/usuario_cadastrar.html', contexto)


# BASEADO NO VÍDEO DE BRUNO - passo 3 - EDIÇÃO de usuário
def editar_usuario(request,id):
    usuario =  Usuario.objects.get(pk=id)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios')
    contexto = {
            'form_usuario': form
        }
    return render(request,'usuarios/usuario_cadastrar.html',contexto)


# BASEADO NO VÍDEO DE BRUNO - passo 4 - REMOÇÃO de usuário
def remover_usuario(request,id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('listar_usuarios')



# BASEADO NO VÍDEO DE BRUNO - passo 1 -LISTAGEM de RESERVATÓRIO
def listar_reservatorio(request):
    reservatorio = Reservatorio.objects.all()
    contexto = {
        'listagem_reservatorios': reservatorio
    }
    return render(request, 'usuarios/listagem_reservatorio.html', contexto)









def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def perfil(request):
    return render(request, 'perfil.html')

def gestor(request):
    return render(request, 'gestor.html')