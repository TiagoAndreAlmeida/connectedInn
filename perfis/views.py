from django.shortcuts import render
from django.http import HttpResponse

from .models import Perfil

# Create your views here.
def index(request):
    return render(request, 'index.html',context={'name': 'tiago'})

def perfis(request, perfil_id):
    
    try:
        perfil = Perfil.objects.get(id=perfil_id)
        return render(request, 'perfis.html', context={'perfil': perfil})
    except:
        return render(request, '404.html')
