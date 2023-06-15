from django.shortcuts import render
from .models import Professor
from .models import Cadastro

def formulario(request):
    professores = ['Orlando Saraiva Jr', 'Thiago Mendes', 'Esdras', 'Nilton', 'Leonardo'] 
    context = {'professores': professores}

    if request.method == 'POST':
        nome = request.POST['nome']
        professor = request.POST['professor']
        cadastro = Cadastro(nome=nome, professor=professor)
        cadastro.save()
        
    
    return render(request, 'formulario.html', context)


def lista(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        professores_selecionados = request.POST.getlist('professor')
        professores = Professor.objects.filter(id__in=professores_selecionados)
        
    cadastros = Cadastro.objects.all()  
    context = {'cadastros': cadastros}
    return render(request, 'lista.html', context)