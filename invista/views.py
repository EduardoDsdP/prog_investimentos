from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm



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


def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentosleitura')    
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request,'investimentos_ps/novo_investimento.html', context=formulario)
    



def editar(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request,'investimentos_ps/novo_investimento.html',{'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST,instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentosleitura')    
    



def excluir(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento) 
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentosleitura')
    return render(request,'investimentos_ps/confirmar_exclusao.html', {'item': investimento})  