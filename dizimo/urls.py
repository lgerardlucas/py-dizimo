from django.contrib import admin
from django.urls import path

# Admin Site Config
admin.sites.AdminSite.site_header = 'Controle de Dizimista'
admin.sites.AdminSite.site_title = 'Controle de Dizimista'
admin.sites.AdminSite.index_title = 'Controle de Dizimista'

urlpatterns = [
    path('', admin.site.urls),
]
