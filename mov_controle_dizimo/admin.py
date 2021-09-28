from django.contrib import admin
from .models import Controle_Dizimo

class Controle_DizimoAdmin(admin.ModelAdmin):
    list_display = ('dizimista', 'ano', 'mes')
    list_diplay_links = ('dizimista',)
    list_filter = ('dizimista', 'ano', 'mes')
    ordering = ['dizimista', 'ano', 'mes']

    save_on_top = False
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

admin.site.register(Controle_Dizimo,Controle_DizimoAdmin)
