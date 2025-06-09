from django.shortcuts import render
from django.http import HttpResponse
from lojaVeiculo.models import *
def list_veiculo_view(request):
    veiculo = request.GET.get("veiculo")
    preco = request.GET.get("preco")
    cor = request.GET.get("cor")
    descricao = request.GET.get("descricao")
    ano = request.GET.get("ano")
    veiculos = Veiculo.objects.all()
    print(veiculos)
    if id is None:
        id = 0
    return HttpResponse('<h1>Lista de Veiculos</h1>')