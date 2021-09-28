from django.db import models

class Missionario(models.Model):
    nome = models.CharField('Nome do Missionário', max_length=200, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Missionário'
        verbose_name_plural = 'Missionários'
        ordering = ['nome']

    def __str__(self):
        return self.nome
