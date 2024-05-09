from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Bem vindo''(a)'' a pagina investimentos! É um prazer ter você aqui.')


def contato(request):
    return HttpResponse('Para duvidas enviar um email para contato@suporte.com')


def termo_politicva_privacidade(request):
    return HttpResponse('Pagina informativa de termo com todos os direitos reservados')


def minha_historia(request):
    pessoa = {
        'nome': 'Eduardo',
        'idade': 32,
        'cargo': 'Analista de Sistemas'
    }
    return render(request,'investimentos_ps/minhaa_historia.html',pessoa)


def novo_investimento(request):
    return render(request,'investimentos_ps/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request,'investimentos_ps/investimento_registrado.html',investimento)