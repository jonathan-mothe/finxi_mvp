from django.contrib import admin
from django.utils.safestring import mark_safe
from api.models import *

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = ['anunciante', 'descricao', 'status_col']


    def status_col(self, obj):
        yes_icon = '<img src="/static/imagens/baseline-check_circle_outline.svg" alt="True">'
        no_icon = '<img src="/static/imagens/baseline-highlight_off.svg" alt="False">'
        
        if obj.status:
            return mark_safe('<a target="_blank" href="%s/change/">%s</a>' % (obj.pk, yes_icon))
        else:
            return mark_safe('<a target="_blank" href="%s/change/">%s</a>' % (obj.pk, no_icon))

    status_col.allow_tags = True
    status_col.short_description = 'Status'