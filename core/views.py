from django.shortcuts import render
from django.contrib import messages  # Biblioteca para aperecer avisos através do código no html boootstrap_message
from .forms import ContatoForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)  # Para poder ou não conter dados

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Email enviado com sucesso')
            form = ContatoForm()  # Limpa o formulaário

        else:
            messages.error(request, 'Erro ao enviar email')

    context = {
        'form': form
    }

    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')

