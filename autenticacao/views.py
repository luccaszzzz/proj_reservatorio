from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar o usuário para outras páginas.
from django.contrib.auth import authenticate, login  # Importa funções para autenticar e fazer login do usuário.
from .forms import CustomUserCreationForm, PerfilForm  # Importa os formulários personalizados para criação de usuário e edição de perfil.
from django.contrib import messages  # Importa o módulo de mensagens para exibir mensagens de sucesso ou erro para o usuário.
from django.contrib.auth.decorators import login_required  # Importa o decorator para garantir que o usuário esteja autenticado antes de acessar a página.


def cadastro(request):  # Função para exibir o formulário de cadastro de usuário.
    if request.method == "POST":  # Verifica se o formulário foi enviado (método POST).
        form = CustomUserCreationForm(
            request.POST
        )  # Cria o formulário com os dados recebidos no POST.
        if form.is_valid():  # Verifica se o formulário é válido (dados corretos).
            user = form.save()  # Salva o novo usuário e retorna a instância criada.
            return redirect(
                "login"
            )  # Redireciona o usuário para a página de login após o cadastro.
    else:
        form = (
            CustomUserCreationForm()
        )  # Exibe um formulário vazio para o usuário preencher.
    return render(
        request, "cadastro.html", {"form": form}
    )  # Renderiza a página de cadastro, passando o formulário para o template.


def user_login(request):  # Função para realizar o login do usuário.
    if (
        request.method == "POST"
    ):  # Verifica se o formulário de login foi enviado (método POST).
        username = request.POST["username"]  # Obtém o nome de usuário enviado.
        password = request.POST["password"]  # Obtém a senha enviada.
        user = authenticate(
            request, username=username, password=password
        )  # Verifica se as credenciais são válidas.

        if user is not None:  # Se o usuário for autenticado com sucesso.
            login(request, user)  # Realiza o login do usuário.
            return redirect(
                "perfil"
            )  # Redireciona para a página de perfil após o login.
        else:
            messages.error(
                request, "Usuário ou senha inválidos."
            )  # Exibe uma mensagem de erro caso as credenciais estejam incorretas.
            return redirect("login")  # Redireciona de volta para a página de login.
    else:
        return render(
            request, "login.html"
        )  # Exibe o formulário de login para o usuário.


@login_required  # Garante que o usuário esteja autenticado antes de acessar a página de perfil.
def perfil(request):  # Função para exibir e editar o perfil do usuário.
    user = request.user  # Obtém o usuário autenticado da sessão.

    if (
        request.method == "POST"
    ):  # Verifica se o formulário de perfil foi enviado (método POST).
        form = PerfilForm(
            request.POST, instance=user
        )  # Cria um formulário preenchido com os dados atuais do usuário.
        if form.is_valid():  # Verifica se o formulário é válido.
            form.save()  # Salva as alterações feitas no perfil do usuário.
            messages.success(
                request, "Perfil atualizado com sucesso!"
            )  # Exibe uma mensagem de sucesso após a atualização.
            return redirect(
                "perfil"
            )  # Redireciona para a página de perfil para exibir as atualizações.
    else:
        form = PerfilForm(
            instance=user
        )  # Preenche o formulário com os dados atuais do usuário.

    return render(
        request, "perfil.html", {"form": form, "user": user}
    )  # Renderiza a página de perfil, passando o formulário e o usuário para o template.
