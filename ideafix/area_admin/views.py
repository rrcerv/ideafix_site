from django.shortcuts import render, redirect
from usuarios.models import Usuario
from area_usuario.models import Projetos
from usuarios import urls as urls_usuario
from django.urls import reverse
import login_admin.views as login_admin_views

def home_admin(request):
    if request.session.get('admin'):
        todos_usuarios = Usuario.objects.all()
        todos_projetos = Projetos.objects.all()
        return render(request, 'home_admin.html', {'todos_usuarios':todos_usuarios, 'todos_projetos':todos_projetos})
    else:
        return redirect(reverse(login_admin_views.login))


def inserir_usuario(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            novo_usuario = Usuario(email = request.POST.get('email'), senha = request.POST.get('senha'), nome = request.POST.get('nome'))
            novo_usuario.save()
        return render(request, 'inserir_usuario.html')
    else:
        return redirect(reverse(login_admin_views.login))

def inserir_projeto(request):
    if request.session.get('admin'):
        todos_usuarios = Usuario.objects.all()
        
        if request.method == 'POST':
            usuario = Usuario.objects.get(nome=request.POST.get('usuario'))
            projeto = request.POST.get('projeto')
            links = request.POST.get('links')
            
            novo_projeto = Projetos(usuario = usuario, projeto = projeto, links = links)
            novo_projeto.save()

            
        return render(request, 'inserir_projeto.html', {'todos_usuarios':todos_usuarios})
    
    else:
        return redirect(reverse(login_admin_views.login))
    
def sair_admin(request):
    url_login_admin = reverse(login_admin_views.login)
    del request.session['admin']
    return redirect(reverse(login_admin_views.login))