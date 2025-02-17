from django.contrib.auth.models import (
    AbstractUser,
)  # Importa a classe AbstractUser para criar um modelo de usuário personalizado que herda do modelo de usuário padrão do Django.
from django.db import (
    models,
)  # Importa o módulo de modelos do Django, necessário para definir campos no banco de dados.


class CustomUser(
    AbstractUser
):  # Cria um modelo de usuário personalizado, que herda os campos padrão de usuário do Django.
    cpf = models.CharField(
        max_length=14, unique=True
    )  # Adiciona o campo CPF, com um tamanho máximo de 14 caracteres e garantindo que seja único.
    telefone = models.CharField(
        max_length=15
    )  # Adiciona o campo de telefone, com um tamanho máximo de 15 caracteres.
    email = models.EmailField(
        unique=True
    )  # Adiciona o campo de e-mail, garantindo que seja único.

    def __str__(
        self,
    ):  # Define a representação em string do modelo, que será o nome de usuário (username).
        return self.username
