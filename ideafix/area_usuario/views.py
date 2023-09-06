from django.shortcuts import render, redirect
from usuarios import urls
from django.urls import reverse
from usuarios.models import Usuario
from .models import Projetos
import usuarios.views as usuarios_views
from django.urls import reverse

def home(request):
    url_sair = (reverse(usuarios_views.sair))
    if request.session.get('usuario'):
        current_user = Usuario.objects.get(id=request.session.get('usuario'))
        projetos_usuario = Projetos.objects.filter(usuario=current_user)

        return render(request,'area_usuario_home.html', {'projetos_usuario' : projetos_usuario, 'url_sair': url_sair})
    else:
        login_url = reverse('login') + '?status=0'
        return redirect('login')
