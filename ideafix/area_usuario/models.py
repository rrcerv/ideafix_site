from django.db import models
from usuarios.models import Usuario

class Projetos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    projeto = models.TextField()
    
class Links_Projetos(models.Model):
    projeto = models.ForeignKey(Projetos, on_delete=models.PROTECT)
    nome_link = models.TextField()
    link = models.TextField()