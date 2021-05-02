from django.db import models


class BasicRoom(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)

    class Meta:
        db_table = "docs_basic_room"
        verbose_name = "Stanza base"
        verbose_name_plural = "Stanze base"

    def __str__(self):
        return f"{self.nome.capitalize()}"


class BasicPosition(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)
    stanza = models.ForeignKey(to="docs.BasicRoom", null=True, blank=True, on_delete=models.CASCADE)
    immagine = models.FileField(null=True, blank=True)
    dettaglio = models.JSONField(null=False, blank=False, default=dict)

    class Meta:
        db_table = "docs_basic_position"
        verbose_name = "Posizione base"
        verbose_name_plural = "Posizione base"

    def __str__(self):
        return f"{self.nome.capitalize()} in {self.stanza.nome().lower()}"


class BasicDoc(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)
    file = models.FileField(null=True, blank=True)
    posizione = models.ForeignKey(to="docs.BasicPosition", null=True, blank=True, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    data_documento = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "docs_basic_doc"
        verbose_name = "Documento base"
        verbose_name_plural = "Documento base"

    def __str__(self):
        return f"Documento {self.nome.capitalize()} del {self.data_documento}"
