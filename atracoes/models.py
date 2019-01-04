from django.db import models
from core.models import PontosTuristicos


class Atracao(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    horario = models.TextField()
    idade_minima = models.IntegerField()
    ponto_turistico = models.ForeignKey(
        PontosTuristicos,
        related_name='ponto_turistico_atracao',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nome
