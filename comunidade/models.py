from django.db import models

class Comunidade(models.Model):
    nome = models.CharField('Nome da Comunidade', max_length=200, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Comunidade'
        verbose_name_plural = 'Comunidades'
        ordering = ['nome']

    def __str__(self):
        return self.nome
