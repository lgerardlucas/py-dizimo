from django.contrib import admin
from .models import Missionario

class MissionarioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_diplay_links = ('nome',)

admin.site.register(Missionario,MissionarioAdmin)
