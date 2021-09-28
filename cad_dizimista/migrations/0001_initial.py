# Generated by Django 3.2.4 on 2021-09-28 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cad_comunidade', '0001_initial'),
        ('cad_missionario', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dizimista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Nome do Dizimista')),
                ('telefone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone')),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Data Nascimento')),
                ('comunidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cad_comunidade', to='cad_comunidade.comunidade', verbose_name='Comunidade')),
                ('missionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cad_missionario', to='cad_missionario.missionario', verbose_name='Missionario')),
            ],
            options={
                'verbose_name': 'Dizimista',
                'verbose_name_plural': 'Dizimistas',
                'ordering': ['nome'],
            },
        ),
    ]
