from django.shortcuts import render,get_object_or_404
from .models import Disease, MedicineDisease

def disease_medicines(request, disease_id):
    disease = get_object_or_404(Disease, pk=disease_id)
    medicines = MedicineDisease.objects.filter(disease=disease).select_related('medicine')
    return render(request, 'disease_medicines.html', {'disease': disease, 'medicines': medicines})
