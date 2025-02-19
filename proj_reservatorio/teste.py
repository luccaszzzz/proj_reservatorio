
from core.views import listar_reservatorio, cadastrar_reservatorio, editar_reservatorio, remover_reservatorio


# CRUD DE RESERVATÓRIO
    path('listar_reservatorio/', listar_reservatorio, name='listar_reservatorio'), # BASEADO NO VÍDEO DE BRUNO - passo 1 - LISTAGEM de RESERVATÓRIO
    path('cadastrar_reservatorio/', cadastrar_reservatorio, name='cadastrar_reservatorio'), # BASEADO NO VÍDEO DE BRUNO - passo 2 - CADASTRO de RESERVATÓRIO
    path('editar_reservatorio/<int:id>/', editar_reservatorio, name='editar_reservatorio'), # BASEADO NO VÍDEO DE BRUNO - passo 3 - EDIÇÃO de RESERVATÓRIO
    path('remover_reservatorio/<int:id>/', remover_reservatorio, name='remover_reservatorio'), # BASEADO NO VÍDEO DE BRUNO - passo 4 - REMOÇÃO de RESERVATÓRIO




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



from .models import Usuario, Reservatorio

class ReservatorioForm(ModelForm):
     class Meta:
          model = Reservatorio 
          fields = ['codigo','senha','tempo','periodicidade']
