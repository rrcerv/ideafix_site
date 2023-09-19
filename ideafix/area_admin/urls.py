from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home_admin, name='home_admin'),
    path('inserir_usuario/', views.inserir_usuario, name='inserir_usuario'),
    path('inserir_projeto/', views.inserir_projeto, name='inserir_projeto'),
    path('sair_admin/', views.sair_admin, name='sair_admin'),
    path('editar_projeto/<int:user_id>/<int:projeto_id>/', views.editar_projeto, name='editar_projeto'),
]