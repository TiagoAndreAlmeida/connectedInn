from django.shortcuts import render
from perfils.models import Perfil

# Create your views here.
def index (request):
    return render(request, 'index.html')

def perfil(request, perfil_id):
    perfil = Perfil('Flavio Almeida', 'flavio@flavio.com.br', '777777', 'Caelum')

    return render(request, 'perfil.html', {"perfil" : perfil})