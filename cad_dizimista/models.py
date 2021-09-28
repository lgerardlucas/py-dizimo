from django.db import models
from datetime import datetime

class Dizimista(models.Model):
    nome = models.CharField('Nome do Dizimista', max_length=200, null=True, blank=True, unique=True)
    telefone = models.CharField('Telefone', max_length=50, null=True, blank=True)
    nascimento = models.DateField('Data Nascimento', null=True, blank=True)
    comunidade = models.ForeignKey('cad_comunidade.Comunidade', on_delete=models.CASCADE, null=True, blank=True, related_name='cad_comunidade', verbose_name='Comunidade')
    missionario = models.ForeignKey('cad_missionario.Missionario', on_delete=models.CASCADE, null=True, blank=True, related_name='cad_missionario', verbose_name='Missionario')

    class Meta:
        verbose_name = 'Dizimista'
        verbose_name_plural = 'Dizimistas'
        ordering = ['nome']

    def __str__(self):
        return self.nome
