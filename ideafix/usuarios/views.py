from django.shortcuts import render
from .models import Usuario
import re
from django.shortcuts import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from django.shortcuts import HttpResponse
import matplotlib.pyplot as plt
from pathlib import Path
import os
from django.urls import reverse
from area_usuario import urls

def login(request):
    status=request.GET.get('status')
    if request.session.get('usuario'):
        return redirect('home_usuario') #LINK PRA HOME DE USUÁRIO
    else:
        return render(request, 'login.html', {'status': status})

def validate_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(Usuario.objects.filter(email=email)) > 0:
            current_user = Usuario.objects.get(email=email)
            if(current_user.senha == senha):
                request.session['usuario'] = current_user.id
                return redirect('home_usuario')
            #if check_password_hash(current_user.senha, senha):
            #    request.session['usuario'] = current_user.id
            #    return redirect('/fitness_app/')
            else:
                return redirect('/auth/login/?status=0')
        else:
            return redirect('/auth/login/?status=1')

def sair(request):
    del request.session['usuario']
    return redirect('/auth/login')