from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)

class Symptom(models.Model):
    name = models.CharField(max_length=255)


class DiseaseSymptom(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('disease', 'symptom')

