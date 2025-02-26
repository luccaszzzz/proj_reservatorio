from django.shortcuts import render, redirect, get_object_or_404 # adicionado dia 13/02 pela vídeo aula de Bruno passo 2 CADASTRAR USUÁRIO
from  .forms import UsuarioForm, ReservatorioForm, MonitoramentoForm # adicionado dia 13/02 pela vídeo aula de Bruno passo 2 CADASTRAR USUÁRIO
from .models import Usuario, Reservatorio, Monitoramento # adicionado dia 14/02 pela vídeo aula de Bruno passo 1 LISTAGEM DE RESERVATÓRIO
from django.core.exceptions import ObjectDoesNotExist # Importa uma exceção para caso um objeto não foi encontrado no banco de dados
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth.hashers import make_password
import requests
import json
from django.http import HttpResponse, JsonResponse

# VIEWS PARA EXPRESS

def listar_usuarios_express(request):
    requisicao = requests.post('http://127.0.0.1:3000/usuarios/list')
    todos = json.loads(requisicao.content)
    return JsonResponse(todos, safe=False)

# Cadastro de usuario comum no express
@login_required(login_url='login')
def cadastrar_usuario_express(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.password = make_password(form.cleaned_data['password'])
        usuario.save()

        # Cadastro no Express
        usuario_express = {
            'nome': usuario.username,
            'email': usuario.email,
            'password': usuario.password,
            'cpf': usuario.cpf,
            'telefone': usuario.celular
        }
        requisicao = requests.post('http://127.0.0.1:3000/signup', data=json.dumps(usuario_express), headers={'Content-Type': 'application/json'})
        return redirect('login')
    
    contexto = {
        'form_usuario': form
    }
    return render(request, 'usuarios/usuario_cadastrar.html', contexto)

def atualizar_usuario_express(request):
    return render(request, 'teste.html')

def excluir_usuario_express(request):
    return render(request, 'teste.html')

# FIM DE VIEWS PARA EXPRESS

def logar(request):
    if request.user.is_authenticated:
        return redirect(reverse('perfil2'))
    if request.POST:
        username = request.POST.get('username')
        print(username)
        senha = request.POST.get('password')
        usuario = authenticate(request, username=username, password=senha)
        print(usuario)
        if usuario is not None:
            login(request, usuario)
            return redirect(reverse('perfil2'))
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def perfil(request):
    return render(request, 'perfil.html')

@login_required(login_url='login')
def perfil2(request):
    return render(request, 'perfil2.html')

def gestor(request):
    return render(request, 'gestor.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

def erro_permissao(request):
    return render(request, 'erro_permissao.html')


# BASEADO NO VÍDEO DE BRUNO - passo 1 -LISTAGEM de usuário
def listar_usuarios(request):  
    query = request.GET.get('search', '')  
    if query:  
        usuarios = Usuario.objects.filter(nome__icontains=query)  # Supondo que "nome" seja um campo do modelo  
    else:  
        usuarios = Usuario.objects.all()  
    
    contexto = {  
        'listagem_usuarios': usuarios,  
        'search_query': query  # Para enviar de volta o termo de busca ao template, se necessário  
    }  
    return render(request, 'usuarios/listar_usuarios.html', contexto) 
    
# Cadastro para usuário master
def cadastrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        celular = request.POST.get('cel')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        usuario = Usuario.objects.create_user(username=username, email=email, cpf=cpf, celular=celular, password=password)
        return redirect('login')
    return render(request, 'cadastro.html')

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
def remover_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('listar_usuarios')

# BASEADO NO VÍDEO DE BRUNO - passo 1 -LISTAGEM de RESERVATÓRIO
def listar_reservatorios(request):  
    query = request.GET.get('search', '')  
    if query:  
        reservatorio = Reservatorio.objects.filter(codigo__icontains=query)  # Supondo que "codigo" seja um campo do modelo  
    else:  
        reservatorio = Reservatorio.objects.all()  

    contexto = {  
        'listagem_reservatorios': reservatorio,  
        'search_query': query  # Para manter o termo de busca no template  
    }  
    return render(request, 'reservatorio/listar_reservatorios.html', contexto)

#CRUD DE RESERVATÓRIOS
# Garante que apenas usuários logados possam acessar essa view
def cadastrar_reservatorio(request):
    form = ReservatorioForm(request.POST or None)
    if form.is_valid():
        reservatorio = form.save(commit=False)  # Não salva no banco ainda

        # Verifica se o usuário está logado
        if request.user.is_authenticated:
            try:
                # Obtém o usuário logado
                usuario_logado = Usuario.objects.get(email=request.user.email) 
                reservatorio.usuario = usuario_logado
            except ObjectDoesNotExist:
                # Caso o usuário logado não tenha um objeto Usuario correspondente
                form.add_error(None, "Usuário não encontrado. Por favor, faça login novamente.")
                return render(request, 'reservatorio/cadastrar_reservatorio.html', {'form_reservatorio': form})
        else:
            # Se o usuário não estiver logado, o campo usuario permanece NULL
            pass

        reservatorio.save()  # Salva o reservatório no banco de dados
        return redirect('listar_reservatorios')  # Redireciona para a lista de reservatórios

    contexto = {
        'form_reservatorio': form
    }
    return render(request, 'reservatorio/cadastrar_reservatorio.html', contexto)


def editar_reservatorio(request,id):
    reservatorio = Reservatorio.objects.get(pk=id)
    form = ReservatorioForm(request.POST or None, instance=reservatorio)
    if form.is_valid():
        form.save()
        return redirect('listar_reservatorios')
    contexto = {
        'form_reservatorio': form
    }
    return render(request, 'reservatorio/cadastrar_reservatorio.html',contexto)

def remover_reservatorio(request,id):
    reservatorio = Reservatorio.objects.get(pk=id)
    reservatorio.delete()
    return redirect('listar_reservatorios')

def detalhe_reservatorio(request, id):
    reservatorio = get_object_or_404(Reservatorio, id=id) # Usa get_object_or_404 para lidar com o erro
    return render(request, 'reservatorio/detalhe_reservatorio.html', {'reservatorio': reservatorio})

#CRUD DE MONITORAMENTO
def listar_monitoramentos(request):  
    query = request.GET.get('search', '')  
    if query:  
        monitoramento = Monitoramento.objects.filter(data_hora__icontains=query)  # Supondo que "data" seja um campo do modelo  
    else:  
        monitoramento = Monitoramento.objects.all()  

    contexto = {  
        'todos_monitoramentos': monitoramento,  
        'search_query': query  # Para manter o termo de busca no template  
    }  
    return render(request, 'monitoramento/listar_monitoramentos.html', contexto)

def cadastrar_monitoramento(request):
    form = MonitoramentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_monitoramentos')
    contexto = {
        'form_monitoramento': form
    }
    return render(request, 'monitoramento/cadastrar_monitoramento.html', contexto)

def editar_monitoramento(request,id):
    monitoramento = Monitoramento.objects.get(pk=id)
    form = MonitoramentoForm(request.POST or None, instance=monitoramento)
    if form.is_valid():
        form.save()
        return redirect('listar_monitoramentos')
    contexto = {
        'form_monitoramento': form
    }
    return render(request, 'monitoramento/cadastrar_monitoramento.html',contexto)

def remover_monitoramento(request,id):
    monitoramento = get_object_or_404(Monitoramento, pk=id) # Usa get_object_or_404 para lidar com o erro
    monitoramento.delete()
    return redirect('listar_monitoramentos')

# @login_required  # Garante que apenas usuários logados possam acessar essa view
# def cadastrar_reservatorio(request):
#     form = ReservatorioForm(request.POST or None)
#     if form.is_valid():
#         reservatorio = form.save(commit=False)  # Não salva no banco ainda
#             # Associa o reservatório ao usuário logado
#             # Aqui, você precisa obter o usuário logado (request.user) e encontrar o objeto Usuario correspondente
#         usuario_logado = Usuario.objects.get(email=request.user.email)  # Supondo que o email seja único
#         reservatorio.usuario = usuario_logado
#         form.save()
#         return redirect('listar_reservatorio')
#     contexto = {
#         'form_reservatorio': form
#     }

#     return render(request, 'reservatorio/cadastrar_reservatorio.html',contexto)

    # return render(request, 'detalhe_reservatorio.html')