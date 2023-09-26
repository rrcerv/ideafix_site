from django.db import models
from usuarios.models import Usuario

class Projetos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    projeto = models.TextField()
    
class Links_Projetos(models.Model):
    STATUS_CHOICES = (
        ('homologation', 'Homologação'),
        ('production', 'Produção'),
        # Add more status options as needed
    )

    projeto = models.ForeignKey(Projetos, on_delete=models.PROTECT, related_name='links_projetos')
    nome_link = models.TextField()
    link = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='homologation')