from django.shortcuts import render
from perfils.models import Perfil

# Create your views here.
def index (request):

    return render(request, 'index.html', {"perfils" : Perfil.objects.all()})

def perfil(request, perfil_id):
    perfils = Perfil.objects.all()
    return render(request, 'perfil.html', {"perfils" : perfils})