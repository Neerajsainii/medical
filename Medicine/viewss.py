from django.shortcuts import render,get_object_or_404
from .models import Disease, MedicineDisease

def treatment(request, disease_id):
    disease = get_object_or_404(Disease, pk=disease_id)
    medicines = MedicineDisease.objects.filter(disease=disease).select_related('medicine')
    return render(request, 'treatment.html', {'disease': disease, 'medicines': medicines})
