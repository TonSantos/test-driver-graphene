import graphene

from graphene_django.types import DjangoObjectType

from .models import Atendimento, Paciente, Profissional, Unidade


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


class Query(object):
    unidade = graphene.Field(UnidadeType, id=graphene.Int(), nome=graphene.String(), endereco=graphene.String())
    all_unidades = graphene.List(UnidadeType)

    all_profissionais = graphene.List(ProfissionalType)
    all_pacientes = graphene.List(PacienteType)
    all_atendimentos = graphene.List(AtendimentoType)

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
        
    def resolve_all_unidades(self, info, **kwargs):
        return Unidade.objects.all()

    def resolve_all_profissionais(self, info, **kwargs):
        return Profissional.objects.all()

    def resolve_all_pacientes(self, info, **kwargs):
        return Paciente.objects.all()

    def resolve_all_atendimentos(self, info, **kwargs):
        return Atendimento.objects.all()

    def resolve_all_atendimentos_paciente(self, info, **kwargs):
        return Atendimento.objects.select_related('paciente').all()

    def resolve_all_atendimentos_profissional(self, info, **kwargs):
        return Atendimento.objects.select_related('profissional').all()

    def resolve_all_atendimentos_unidade(self, info, **kwargs):
        return Atendimento.objects.select_related('unidade').all()