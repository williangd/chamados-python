from django.db import models

class Solicitante(models.Model):
    nome = models.CharField(max_length=100)
#    default = models.BooleanField(default=False)


class Empresa(models.Model):
    nome = models.CharField(max_length=200)


class Status(models.Model):
    nome = models.CharField(max_length=100)



class Chamado(models.Model):
    abertura = models.DateTimeField()
    fechamento = models.DateTimeField(blank=True, null=True)
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    problema = models.TextField(blank=True, null=True)