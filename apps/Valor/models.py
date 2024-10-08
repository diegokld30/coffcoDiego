from django.db import models
from apps.Servicio.models import Servicio
from apps.Variables.models import Variables
class Valor(models.Model):
    valor = models.CharField(max_length=45)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    variables = models.ForeignKey(Variables, on_delete=models.CASCADE)

    def __str__(self):
        return self.valor

