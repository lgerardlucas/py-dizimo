from django.contrib import admin
from .models import Comunidade

class ComunidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_diplay_links = ('nome',)

admin.site.register(Comunidade,ComunidadeAdmin)
