from django import (
    forms,
)  # Importa o módulo de formulários do Django, necessário para criar campos e validar dados.
from django.contrib.auth.forms import (
    UserCreationForm,
)  # Importa o formulário de criação de usuário padrão do Django.
from .models import (
    CustomUser,
)  # Importa o modelo CustomUser, que provavelmente é uma extensão do modelo de usuário padrão.
from django.contrib.auth import (
    get_user_model,
)  # Importa a função que retorna o modelo de usuário atualmente ativo no projeto (pode ser CustomUser).


class CustomUserCreationForm(
    UserCreationForm
):  # Cria um formulário personalizado para a criação de usuários, estendendo o formulário padrão de criação de usuário do Django.
    email = forms.EmailField(required=True)  # Adiciona um campo de e-mail obrigatório.
    cpf = forms.CharField(
        max_length=14, required=True
    )  # Adiciona um campo de CPF (máximo de 14 caracteres), obrigatório.
    telefone = forms.CharField(
        max_length=15, required=True
    )  # Adiciona um campo de telefone (máximo de 15 caracteres), obrigatório.

    class Meta:  # A classe Meta é usada para configurar o modelo e os campos do formulário.
        model = (
            CustomUser  # Define que o formulário está associado ao modelo CustomUser.
        )
        fields = (
            "username",
            "email",
            "cpf",
            "telefone",
            "password1",
            "password2",
        )  # Define quais campos do modelo CustomUser aparecerão no formulário (inclui campos do modelo e os de senha).


User = (
    get_user_model()
)  # Obtém o modelo de usuário atualmente em uso no projeto (pode ser o modelo padrão ou um personalizado, como o CustomUser).


class PerfilForm(
    forms.ModelForm
):  # Cria um formulário baseado no modelo, permitindo editar informações do usuário.
    class Meta:  # Configurações de associação do formulário com o modelo e campos a serem usados.
        model = CustomUser  # Especifica que o formulário usa o modelo CustomUser.
        fields = ["username", "email", "telefone"]  # Campos que podem ser editados
