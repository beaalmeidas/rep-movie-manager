from django.db import models


class Movies(models.Model):
    nome = models.CharField(max_length=50)
    lançamento = models.CharField(max_length=10)
    diretor = models.CharField(max_length=50)
    sinopse = models.CharField(max_length=255)
    nota = models.CharField(max_length=10)
    comentario = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)

