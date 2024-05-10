from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def novo_usuario(request):
    # tipo, validar, informar, salvar:
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # informar o usuario
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuario {usuario} foi criado com sucesso!')
            return redirect('login')
            # salvar no banco de dados
    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', {'formulario': formulario})
