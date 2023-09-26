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

def editar_projeto(request, user_id, projeto_id):
    if request.session.get('admin'):
        todos_usuarios = Usuario.objects.all()
        todos_usuarios_ls = []

        try:
            # Retrieve the user and project to edit
            usuario = Usuario.objects.get(pk=user_id)
            projeto = Projetos.objects.get(pk=projeto_id, usuario=usuario)
        except (Usuario.DoesNotExist, Projetos.DoesNotExist):
            # Handle the case where the user or project does not exist
            return redirect(reverse('home_admin'))  # Redirect to the home page or an error page

        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'remove_link':
                link_id = request.POST.get('link_id')
                print(link_id)
                try:
                    link = Links_Projetos.objects.get(pk=link_id,projeto=projeto)
                    link.delete()
                    # Optionally, you can return a success message or redirect back to the edit page
                except Links_Projetos.DoesNotExist:
                    # Handle the case where the link doesn't exist
                    pass
            else:

                # Handle form submission for updating the project
                projeto.projeto = request.POST.get('projeto')
                projeto.save()
                print(request.POST.getlist('link_name'))
                # Retrieve link data based on the form structure
                link_ids = request.POST.getlist('link_id')
                link_names = request.POST.getlist('link_name')
                links = request.POST.getlist('link_url')
                links_status = request.POST.getlist('link_status')
                # Update or create link objects based on the submitted data
                for link_id, link_name, link_url, link_status in zip(link_ids, link_names, links, links_status):

                    if link_id != "novo":

                        # Update an existing link
                        link = Links_Projetos.objects.get(pk=link_id)
                        link.link = link_url
                        link.nome_link = link_name
                        link.status = link_status
                        link.save()
                    else:
                        # Create a new link

                        novo_link = Links_Projetos(link=link_url, projeto=projeto, nome_link=link_name, status=link_status)
                        novo_link.save()

                # Check if new link data is provided and create a new link
                new_link_name = request.POST.getlist('new_link_name')
                new_link_url = request.POST.getlist('new_link_url')

                for link_name, link_url in zip(new_link_name, new_link_url):
                    if link_name and link_url:
                        novo_link = Links_Projetos(link=link_url, projeto=projeto, nome_link=link_name)
                        novo_link.save()

        for usuarios in todos_usuarios:
            todos_usuarios_ls.append(usuarios.nome)

        users_dic = {'usuarios': todos_usuarios_ls}

        context = {
            'todos_usuarios': todos_usuarios,
            'todos_usuarios_ls': users_dic,
            'projeto': projeto,
            'links_projetos': projeto.links_projetos.all()  # Get all links associated with the project
        }

        return render(request, 'editar_projeto.html', context)

    else:
        return redirect(reverse(login_admin_views.login))
def sair_admin(request):
    url_login_admin = reverse(login_admin_views.login)
    del request.session['admin']
    return redirect(reverse(login_admin_views.login))