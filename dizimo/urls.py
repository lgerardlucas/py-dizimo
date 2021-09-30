from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Admin Site Config
admin.sites.AdminSite.site_header = 'Controle de Dizimista'
admin.sites.AdminSite.site_title = 'Controle de Dizimista'
admin.sites.AdminSite.index_title = 'Controle de Dizimista'

urlpatterns = [
    path('', admin.site.urls),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
