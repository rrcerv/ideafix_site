from django.shortcuts import render, redirect
from usuarios.models import Usuario
from area_usuario.models import Projetos, Links_Projetos
from usuarios import urls as urls_usuario
from django.urls import reverse
import login_admin.views as login_admin_views
import json

def home_admin(request):
    if request.session.get('admin'):
        todos_usuarios = Usuario.objects.all()
        todos_projetos = Projetos.objects.all()
        todos_links = Links_Projetos.objects.all()
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
        todos_usuarios_ls = []

        if request.method == 'POST':
            usuario = Usuario.objects.get(nome=request.POST.get('nome'))
            projeto = request.POST.get('projeto')
            novo_projeto = Projetos(usuario=usuario, projeto=projeto)
            novo_projeto.save()

            # Retrieve link data based on the new form structure
            link_names = request.POST.getlist('link_name')
            links = request.POST.getlist('link_url')

            # Iterate through the submitted links and their names
            for link_name, link_url in zip(link_names, links):
                novo_link = Links_Projetos(link=link_url, projeto=novo_projeto, nome_link=link_name)
                novo_link.save()

        for usuarios in todos_usuarios:
            todos_usuarios_ls.append(usuarios.nome)

        users_dic = {'usuarios': todos_usuarios_ls}

        context = {"my_list": ["item1", "item2"]}

        return render(request, 'inserir_projeto.html', {'todos_usuarios': todos_usuarios, 'todos_usuarios_ls': users_dic, 'context': context})

    else:
        return redirect(reverse(login_admin_views.login))
def sair_admin(request):
    url_login_admin = reverse(login_admin_views.login)
    del request.session['admin']
    return redirect(reverse(login_admin_views.login))