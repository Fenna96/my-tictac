from django.db import models
from .basics import BasicDoc


class Invoice(models.BasicDoc):
    spesa = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "docs_invoice"
        verbose_name = "Fattura"
        verbose_name_plural = "Fatture"