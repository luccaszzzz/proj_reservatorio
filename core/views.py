from django.shortcuts import render

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

def usuario_listar(request):
    return render(request, 'usuario_listar.html')

def reservatorio_listar(request):
    return render(request, 'reservatorio_listar.html')

def monitoramento_listar(request):
    return render(request, 'monitoramento_listar.html')