from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Solicitacao

def solicitacao(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        if not nome or not descricao:
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'solicitacao.html')
        Solicitacao.objects.create(nome=nome, descricao=descricao)
        messages.success(request, "Solicitação enviada com sucesso!")
        return redirect('solicitacao')
    
    return render(request, 'solicitacao.html')