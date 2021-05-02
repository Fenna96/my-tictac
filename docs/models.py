from django.db import models


class BasicPosition(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)
    immagine = models.FileField(null=True, blank=True)
    dettaglio = models.JSONField(null=False, blank=False, default={})


# Create your models here.
class BasicDoc(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)
    file = models.FileField(null=True, blank=True)
    posizione = models.ForeignKey(to="docs.BasicPosition", null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    data_documento = models.DateField(null=True, blank=True)
