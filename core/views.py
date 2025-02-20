from django.shortcuts import render, redirect #adicionado dia 13/02 pela vídeo aula de Bruno passo 2 CADASTRAR USUÁRIO
# from .models import Usuario #adicionado dia 13/02 pela vídeo aula de Bruno passo 1 LOGIN REGISTRAR USUÁRIO
from  .forms import UsuarioForm, ReservatorioForm, MonitoramentoForm #adicionado dia 13/02 pela vídeo aula de Bruno passo 2 CADASTRAR USUÁRIO
from .models import Reservatorio,Usuario, Monitoramento #adicionado dia 14/02 pela vídeo aula de Bruno passo 1 LISTAGEM DE RESERVATÓRIO
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


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

def usuario_listar2(request):
    return render(request, 'usuario_listar2.html')

def reservatorio_listar(request):
    return render(request, 'reservatorio_listar.html')

def monitoramento_listar(request):
    return render(request, 'monitoramento_listar.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def detalhe_reservatorio(request):
    return render(request, 'cadastro.html')

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
    return render(request, 'reservatorio/listar_reservatorio.html', contexto)


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
        return redirect('listar_reservatorio')  # Redireciona para a lista de reservatórios

    contexto = {
        'form_reservatorio': form
    }
    return render(request, 'reservatorio/cadastrar_reservatorio.html', contexto)


def editar_reservatorio(request,id):
    reservatorio = Reservatorio.objects.get(pk=id)
    form = ReservatorioForm(request.POST or None, instance=reservatorio)
    if form.is_valid():
        form.save()
        return redirect('listar_reservatorio')
    contexto = {
        'form_reservatorio': form
    }
    return render(request, 'reservatorio/cadastrar_reservatorio.html',contexto)

def remover_reservatorio(request,id):
    reservatorio = Reservatorio.objects.get(pk=id)
    reservatorio.delete()
    return redirect('listar_reservatorio')



#CRUD DE MONITORAMENTO
def listar_monitoramento(request):
    monitoramento = Monitoramento.objects.all()
    contexto = {    
        'todos_monitoramentos': monitoramento
    }
    return render(request, 'monitoramento/listar_monitoramento.html', contexto)

def cadastrar_monitoramento(request):
    form = MonitoramentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_monitoramento')
    contexto = {
        'form_monitoramento': form
    }
    return render(request, 'monitoramento/cadastrar_monitoramento.html', contexto)

def editar_monitoramento(request,id):
    monitoramento = Monitoramento.objects.get(pk=id)
    form = MonitoramentoForm(request.POST or None, instance=monitoramento)
    if form.is_valid():
        form.save()
        return redirect('listar_monitoramento')
    contexto = {
        'form_monitoramento': form
    }
    return render(request, 'monitoramento/cadastrar_monitoramento.html',contexto)

def remover_monitoramento(request,id):
    monitoramento = Monitoramento.objects.get(pk=id)
    monitoramento.delete()
    return redirect('listar_monitoramento')







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