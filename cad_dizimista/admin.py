from django.contrib import admin
from .models import Dizimista
from  django.contrib.auth.models  import  Group, User

admin.site.unregister(Group)
admin.site.unregister(User)

class DizimistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'nascimento', 'comunidade', 'missionario')
    list_diplay_links = ('nome',)

    list_filter = ('nome','missionario')
    search_fields = ('nome', 'telefone', 'nascimento',)

    save_on_top = False
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

admin.site.register(Dizimista,DizimistaAdmin)
