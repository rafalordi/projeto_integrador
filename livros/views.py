from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Emprestimos, Livros

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.all()
        return render(request, 'home.html', {'livros': livros, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/auth/login/?status=2')

def ver_livro(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        emprestimos = Emprestimos.objects.filter(livro = livros)
        return render(request, 'ver_livro.html', {'livro': livros, 'emprestimos': emprestimos, 'usuario_logado': request.session.get('usuario')})
    return redirect('/auth/login/?status=2')