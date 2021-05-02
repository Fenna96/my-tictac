from django.db import models
from .basics import BasicDoc


class Speciality(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)

    class Meta:
        db_table = "docs_speciality"
        verbose_name = "Specializzazione"
        verbose_name_plural = "Specializzazioni"

    def __str__(self):
        return f"{self.nome.capitalize()}"


class Doctor(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)
    specializzazione = models.ForeignKey(to="docs.Speciality", null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "docs_doctor"
        verbose_name = "Dottore"
        verbose_name_plural = "Dottori"

    def __str__(self):
        return f"{self.nome.capitalize()}, {self.mansione.nome.capitalize()}"


class MedicalDoc(BasicDoc):
    spesa = models.FloatField(null=True, blank=True)
    medico = models.ForeignKey(to="docs.Doctor", null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "docs_medical_doc"
        verbose_name = "Documento medico"
        verbose_name_plural = "Documenti medici"