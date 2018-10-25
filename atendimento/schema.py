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
    pacientes = graphene.List(PacienteType)
    paciente = graphene.Field(PacienteType, id=graphene.Int(), nome=graphene.String(), cpf=graphene.String())

    unidades = graphene.List(UnidadeType)
    unidade = graphene.Field(UnidadeType, id=graphene.Int(), nome=graphene.String(), endereco=graphene.String())

    profissionais = graphene.List(ProfissionalType)
    profissional = graphene.Field(ProfissionalType, id=graphene.Int(), nome=graphene.String(), crm=graphene.String())

    atendimentos  = graphene.List(AtendimentoType)

    diagnosticos  = graphene.List(DiagnosticoType)
    diagnostico = graphene.Field(DiagnosticoType, id=graphene.Int(), cid10=graphene.String())

    tratamentos   = graphene.List(TratamentoType)
    exames        = graphene.List(ExameType)
    procedimentos = graphene.List(ProcedimentoType)
    medicamentos  = graphene.List(MedicamentoType)

    def resolve_pacientes(self, info, **kwargs):
        return Paciente.objects.all()

    def resolve_paciente(self, info, **kwargs):
        for field in Paciente._meta.get_fields():
            if kwargs.get(field.name) is not None:
                return Paciente.objects.get(**{field.name:kwargs.get(field.name)}) 
        return None

    def resolve_unidades(self, info, **kwargs):
        return Unidade.objects.all()

    def resolve_unidade(self, info, **kwargs):
        for field in Unidade._meta.get_fields():
            if kwargs.get(field.name) is not None:
                return Unidade.objects.get(**{field.name:kwargs.get(field.name)}) 
        return None

    def resolve_profissionais(self, info, **kwargs):
        return Profissional.objects.all()

    def resolve_profissional(self, info, **kwargs):
        for field in Profissional._meta.get_fields():
            if kwargs.get(field.name) is not None:
                return Profissional.objects.get(**{field.name:kwargs.get(field.name)}) 
        return None

    def resolve_atendimentos(self, info, **kwargs):
        return Atendimento.objects.all()

    def resolve_diagnosticos(self, info, **kwargs):
        return Diagnostico.objects.all()

    def resolve_tratamentos(self, info, **kwargs):
        return Tratamento.objects.all()

    def resolve_exames(self, info, **kwargs):
        return Exame.objects.all()

    def resolve_procedimentos(self, info, **kwargs):
        return Procedimento.objects.all()

    def resolve_medicamentos(self, info, **kwargs):
        return Medicamento.objects.all()

    def resolve_atendimentos_paciente(self, info, **kwargs):
        return Atendimento.objects.select_related('paciente').all()

    def resolve_atendimentos_profissional(self, info, **kwargs):
        return Atendimento.objects.select_related('profissional').all()

    def resolve_atendimentos_unidade(self, info, **kwargs):
        return Atendimento.objects.select_related('unidade').all()

    def resolve_diagnosticos_atendimento(self, info, **kwargs):
        return Diagnostico.objects.select_related('atendimento').all()


# Mutations
#1
class CreatePaciente(graphene.Mutation):
    id = graphene.Int()
    nome = graphene.String()
    cpf = graphene.String()

    #2
    class Arguments:
        nome = graphene.String()
        cpf = graphene.String()

    #3
    def mutate(self, nome, cpf):
        paciente = Paciente(nome=nome, cpf=cpf)
        paciente.save()

        return CreatePaciente(
            id=paciente.id,
            nome=paciente.nome,
            cpf=paciente.cpf,
        )


#4
class Mutation(graphene.ObjectType):
    create_paciente = CreatePaciente.Field()