from django.db import models
from usuarios.models import Usuario

class Projetos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    projeto = models.TextField()
    links = models.TextField()

    def links_as_list(self):
        return self.links.split(',')