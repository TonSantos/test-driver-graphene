import graphene

from graphene_django.types import DjangoObjectType

from .models import (Unidade, Diagnostico,
                     Profissional, Tratamento,
                     Paciente, Exame, Procedimento,
                     Atendimento, Medicamento)


class PacienteType(DjangoObjectType):
    class Meta:
        model = Paciente

class ProfissionalType(DjangoObjectType):
    class Meta:
        model = Profissional

class UnidadeType(DjangoObjectType):
    class Meta:
        model = Unidade

class AtendimentoType(DjangoObjectType):
    class Meta:
        model = Atendimento

class DiagnosticoType(DjangoObjectType):
    class Meta:
        model = Diagnostico

class TratamentoType(DjangoObjectType):
    class Meta:
        model = Tratamento

class ExameType(DjangoObjectType):
    class Meta:
        model = Exame

class ProcedimentoType(DjangoObjectType):
    class Meta:
        model = Procedimento

class MedicamentoType(DjangoObjectType):
    class Meta:
        model = Medicamento


class Query(graphene.ObjectType):
    all_unidades = graphene.List(UnidadeType)
    unidade = graphene.Field(UnidadeType, id=graphene.Int(), nome=graphene.String(), endereco=graphene.String())

    all_profissionais = graphene.List(ProfissionalType)
    profissional = graphene.Field(ProfissionalType, id=graphene.Int(), nome=graphene.String(), crm=graphene.String())

    all_pacientes     = graphene.List(PacienteType)
    paciente = graphene.Field(PacienteType, id=graphene.Int(), nome=graphene.String(), cpf=graphene.String())

    all_atendimentos  = graphene.List(AtendimentoType)

    all_diagnosticos  = graphene.List(DiagnosticoType)
    diagnostico = graphene.Field(DiagnosticoType, id=graphene.Int(), cid10=graphene.String())

    all_tratamentos   = graphene.List(TratamentoType)
    all_exames        = graphene.List(ExameType)
    all_procedimentos = graphene.List(ProcedimentoType)
    all_medicamentos  = graphene.List(MedicamentoType)

    def resolve_all_unidades(self, info, **kwargs):
        return Unidade.objects.all()

    def resolve_unidade(self, info, **kwargs):
        for field in Unidade._meta.get_fields():
            if kwargs.get(field.name) is not None:
                return Unidade.objects.get(**{field.name:kwargs.get(field.name)}) 
        return None

    def resolve_all_profissionais(self, info, **kwargs):
        return Profissional.objects.all()

    def resolve_profissional(self, info, **kwargs):
        for field in Profissional._meta.get_fields():
            if kwargs.get(field.name) is not None:
                return Profissional.objects.get(**{field.name:kwargs.get(field.name)}) 
        return None

    def resolve_all_pacientes(self, info, **kwargs):
        return Paciente.objects.all()

    def resolve_paciente(self, info, **kwargs):
        for field in Paciente._meta.get_fields():
            if kwargs.get(field.name) is not None:
                return Paciente.objects.get(**{field.name:kwargs.get(field.name)}) 
        return None

    def resolve_all_atendimentos(self, info, **kwargs):
        return Atendimento.objects.all()

    def resolve_all_diagnosticos(self, info, **kwargs):
        return Diagnostico.objects.all()

    def resolve_all_tratamentos(self, info, **kwargs):
        return Tratamento.objects.all()

    def resolve_all_exames(self, info, **kwargs):
        return Exame.objects.all()

    def resolve_all_procedimentos(self, info, **kwargs):
        return Procedimento.objects.all()

    def resolve_all_medicamentos(self, info, **kwargs):
        return Medicamento.objects.all()

    def resolve_all_atendimentos_paciente(self, info, **kwargs):
        return Atendimento.objects.select_related('paciente').all()

    def resolve_all_atendimentos_profissional(self, info, **kwargs):
        return Atendimento.objects.select_related('profissional').all()

    def resolve_all_atendimentos_unidade(self, info, **kwargs):
        return Atendimento.objects.select_related('unidade').all()

    def resolve_all_diagnosticos_atendimento(self, info, **kwargs):
        return Diagnostico.objects.select_related('atendimento').all()