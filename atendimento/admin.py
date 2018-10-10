from django.contrib import admin

from .models import Unidade, Profissional, Paciente, Atendimento

admin.site.register(Unidade)
admin.site.register(Profissional)
admin.site.register(Paciente)
admin.site.register(Atendimento)