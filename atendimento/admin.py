from django.contrib import admin

from .models import (Unidade, Diagnostico,
                     Profissional, Tratamento,
                     Paciente, Exame, Procedimento,
                     Atendimento, Medicamento)

admin.site.register(Unidade)
admin.site.register(Profissional)
admin.site.register(Paciente)
admin.site.register(Atendimento)
admin.site.register(Diagnostico)
admin.site.register(Tratamento)
admin.site.register(Exame)
admin.site.register(Procedimento)
admin.site.register(Medicamento)