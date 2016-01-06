from django.contrib import admin
from django.utils.timezone import now
from .models import Solicitante, Empresa, Status, Chamado

class ChamadoModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'empresa', 'solicitante', 'abertura', 'fechamento')
    date_hierarchy = 'abertura'
    search_fields = ('titulo',)
    list_filter = ('abertura',)     


admin.site.register(Solicitante)
admin.site.register(Empresa)
admin.site.register(Status)
admin.site.register(Chamado, ChamadoModelAdmin)
