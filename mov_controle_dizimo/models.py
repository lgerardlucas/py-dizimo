from django.db import models

ANO_CHOICES = (
        (2020, 2020),
        (2021, 2021),
        (2022, 2022)
)
MES_CHOICES = (
        ('01', 'Janeiro'),
        ('02', 'Fevereiro'),
        ('03', 'Março'),
        ('04', 'Abril'),
        ('05', 'Maio'),
        ('06', 'Junho'),
        ('07', 'Julho'),
        ('08', 'Agosto'),
        ('09', 'Setembro'),
        ('10', 'Outubro'),
        ('11', 'Novembro'),
        ('12', 'Dezembro')
)

class Controle_Dizimo(models.Model):
    dizimista = models.ForeignKey('dizimista.Dizimista', on_delete=models.CASCADE, null=True, blank=True, related_name='dizimista_controle', verbose_name='Dizimista-Controle')
    ano = models.IntegerField('Ano', choices=ANO_CHOICES, null=False, blank=False)
    mes = models.CharField('Mês',max_length=2, choices=MES_CHOICES, null=False, blank=False)

    class Meta:
        verbose_name = 'Controle-Dízimo'
        verbose_name_plural = 'Controle-Dízimos'
        ordering = ['ano','mes',]

    def __str__(self):
        return self.dizimista.nome
