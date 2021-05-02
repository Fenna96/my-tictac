from django.db import models
from .basics import BasicDoc


class Paycheck(BasicDoc):
    totale = models.FloatField(null=False, blank=False)
    trattenute = models.FloatField(null=False, blank=False)
    TRF = models.FloatField(null=False, blank=False)
    giorni = models.IntegerField(null=False, blank=False)
    bonus_renzi = models.FloatField(null=False, blank=False)

    class Meta:
        db_table = "docs_paycheck"
        verbose_name = "Busta paga"
        verbose_name_plural = "Buste paga"
