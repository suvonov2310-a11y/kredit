from django.db import models

class Bank(models.Model):
    nomi = models.CharField("Bank nomi", max_length=100)
    foiz = models.FloatField("Yillik foiz stavkasi")
    foyda = models.TextField("Ijobiy tomonlari")
    zarar = models.TextField("Kamchiliklari/Risklar")

    class Meta:
        verbose_name_plural = "Banklar"

    def __str__(self):
        return self.nomi