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


class Query(object):
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
        id = kwargs.get('id')
        nome = kwargs.get('nome')
        endereco = kwargs.get('endereco')

        if id is not None:
            return Unidade.objects.get(pk=id)

        if nome is not None:
            return Unidade.objects.get(nome=nome)
        
        if endereco is not None:
            return Unidade.objects.get(endereco=endereco)

        return None

    def resolve_all_profissionais(self, info, **kwargs):
        return Profissional.objects.all()

    def resolve_profissional(self, info, **kwargs):
        id = kwargs.get('id')
        nome = kwargs.get('nome')
        crm = kwargs.get('crm')

        if id is not None:
            return Profissional.objects.get(pk=id)

        if nome is not None:
            return Profissional.objects.get(nome=nome)
        
        if crm is not None:
            return Profissional.objects.get(crm=crm)

        return None

    def resolve_all_pacientes(self, info, **kwargs):
        return Paciente.objects.all()

    def resolve_all_atendimentos(self, info, **kwargs):
        return Atendimento.objects.all()

    def resolve_all_diagnosticos(self, info, **kwargs):
        descricao = kwargs.get('descricao')
        if descricao is not None:
            return Diagnostico.objects.filter(descricao__contains=descricao)

        return Diagnostico.objects.all()

    def resolve_diagnostico(self, info, **kwargs):
        id = kwargs.get('id')
        cid10 = kwargs.get('cid10')

        if id is not None:
            return Diagnostico.objects.get(pk=id)

        if cid10 is not None:
            return Diagnostico.objects.get(cid10=cid10)

        return None

    def resolve_all_tratamentos(self, info, **kwargs):
        return Tratamento.objects.all()

    def resolve_all_exames(self, info, **kwargs):
        return Exame.objects.all()

    def resolve_all_procedimento(self, info, **kwargs):
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