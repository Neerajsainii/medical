from django.db import models
from Symptom.models import Disease
class Medicine(models.Model):
    name = models.CharField(max_length=255)

class MedicineDisease(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('medicine','disease')
