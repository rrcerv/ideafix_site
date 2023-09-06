from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('login/', views.login, name='login_admin'),
    path('validate_login/', views.validate_login, name='validate_login_admin'),
    path('sair/', views.sair, name='sair_admin'),
    path('home/', views.home, name='home_admin'),
]