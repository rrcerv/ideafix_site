from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=250)
    nome = models.TextField(max_length=20)

    def __str__(self) -> str:
        return self.email 