from django.shortcuts import render
from .models import Admin
import re
from django.shortcuts import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from django.shortcuts import HttpResponse
import matplotlib.pyplot as plt
from pathlib import Path
from django.urls import reverse
import os

def login(request):
    status=request.GET.get('status')
    if request.session.get('admin'):
        return redirect('home_admin')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            senha = request.POST.get('senha')

            if len(Admin.objects.filter(email=email)) > 0:
                current_user = Admin.objects.get(email=email)
            
            #if check_password_hash(current_user.senha, senha):
            #    request.session['admin'] = current_user.id
            #    return redirect('/fitness_app/') 
            
            if current_user.senha == senha:
                request.session['admin'] = current_user.id
                print('Oh yes')
                return redirect('home_admin')
            
            else:
                login_url = reverse('login_admin') + '?status=0'
                return redirect(login_url)

        return render(request, 'login_admin.html', {'status': status})

def validate_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(Admin.objects.filter(email=email)) > 0:
            current_user = Admin.objects.get(email=email)
            
            #if check_password_hash(current_user.senha, senha):
            #    request.session['admin'] = current_user.id
            #    return redirect('/fitness_app/') 
            
            if current_user.senha == senha:
                request.session['admin'] = current_user.id
                print('Oh yes')
                return redirect('home_admin')

            
            else:
                login_url = reverse('login_admin') + '?status=0'
                return redirect(login_url)
        
        else:
            login_url = reverse('login_admin') + '?status=1'
            return redirect(login_url)
        
def home(request):
    if request.session.get('admin'):
        return render(request, 'home_admin.html')
    else:
        url_acesso_nao_autorizado = reverse('login_admin') + '?status=2'
        return redirect(url_acesso_nao_autorizado)

def sair(request):
    request.session.flush()
    return redirect('login_admin')