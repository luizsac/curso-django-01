from django.shortcuts import render, get_object_or_404

from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {'curso': 'Programação Web com Django Framework',
               'produtos': produtos
               }
    return render(request, 'index.html', context)

def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {'produto': prod}
    return render(request, 'produto.html', context)

