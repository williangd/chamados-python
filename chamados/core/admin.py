from django.contrib import admin
from .models import Solicitante, Empresa, Status, Chamado

admin.site.register(Solicitante)
admin.site.register(Empresa)
admin.site.register(Status)
admin.site.register(Chamado)
