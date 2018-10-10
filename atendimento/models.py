from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    cpf  = models.CharField(max_length=15)

class Profissional(models.Model):
    nome = models.CharField(max_length=50)
    crm  = models.CharField(max_length=10)

class Unidade(models.Model):
    nome = models.CharField(max_length=50)
    endereco  = models.CharField(max_length=255)

class Atendimento(models.Model):
    criado_em     = models.DateTimeField(auto_now_add=True)
    finalizado_em = models.DateTimeField(null=True)
    paciente = models.ForeignKey(Paciente, related_name='atendimentos', on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, related_name='atendimentos', on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, related_name='atendimentos', on_delete=models.CASCADE)

class Diagnostico(models.Model):
    cid10 = models.CharField(max_length=8)
    descricao = models.TextField(null=True)
    atendimento = models.ForeignKey(Atendimento, related_name='diagnosticos', on_delete=models.CASCADE)

class Tratamento(models.Model):
    descricao = models.TextField()
    atendimento = models.ForeignKey(Atendimento, related_name='tratamentos', on_delete=models.CASCADE)

class Procedimento(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    tratamento = models.ForeignKey(Tratamento, related_name='procedimentos', on_delete=models.CASCADE)

class Medicamento(models.Model):
    nome = models.CharField(max_length=80)
    dose = models.FloatField()
    posologia = models.CharField(max_length=120)
    tratamento = models.ForeignKey(Tratamento, related_name='medicamentos', on_delete=models.CASCADE)

class Exame(models.Model):
    nome = models.CharField(max_length=80)
    resultado = models.CharField(max_length=150)
    tratamento = models.ForeignKey(Tratamento, related_name='exames', on_delete=models.CASCADE)