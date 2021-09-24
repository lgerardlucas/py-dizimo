from django.db import models

class Dizimista(models.Model):
    nome = models.CharField('Nome do Dizimista', max_length=200, null=True, blank=True, unique=True)
    telefone = models.CharField('Telefone', max_length=50, null=True, blank=True)
    nascimento = models.DateField('Data Nascimento', null=True, blank=True)
    comunidade = models.ForeignKey('comunidade.Comunidade', on_delete=models.CASCADE, null=True, blank=True, related_name='comunidade', verbose_name='Comunidade')

    class Meta:
        verbose_name = 'Dizimista'
        verbose_name_plural = 'Dizimistas'
        ordering = ['nome']

    def __str__(self):
        return self.nome
