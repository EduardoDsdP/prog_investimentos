"""
URL configuration for prog_investimentos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invista import views
from usuarios import views as usuario_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('conta/',usuario_views.novo_usuario,name='novo_usuario'),
    path('',views.investimentos_leitura, name='investimentosleitura'), 
    path('contato/',views.contato, name='contato'),
    path('termo/',views.termo_politicva_privacidade),
    path('minhaa_historia/',views.minha_historia,name='minhaa_historia'),
    path('novo_investimento/',views.criar,name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>',views.editar,name='editar'),
    path('excluir_investimento/<int:id_investimento>',views.excluir,name='excluir'),
    path('investimento_registrado/',views.investimento_registrado, name='investimento_registrado'),
    path('/<int:id_investimento>',views.detalhe,name='detalhe')
]
