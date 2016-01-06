from django.db import models

class Solicitante(models.Model):
    nome = models.CharField(max_length=100)
#    default = models.BooleanField(default=False)
    def __str__(self):
        return self.nome


class Empresa(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Status(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Chamado(models.Model):
    abertura = models.DateTimeField('abertura',)
    fechamento = models.DateTimeField('fechamento', blank=True, null=True)
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    titulo = models.CharField('título', blank=True, null=True, max_length=200)
    problema = models.TextField('problema', blank=True, null=True)


    class Meta:
            verbose_name_plural = 'chamados'
            verbose_name = 'chamado'
            ordering = ('-abertura',)

    #def __str__(self):
    #    return self.titulo