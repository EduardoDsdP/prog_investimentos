from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Investimento



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

def investimentos_leitura(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request,'investimentos_ps/investimentosleitura.html',context=dados)


def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)   
    }
    return render(request,'investimentos_ps/detalhe.html',dados)
