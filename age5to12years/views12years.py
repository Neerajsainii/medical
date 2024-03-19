from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .models import Disease, Symptom , DiseaseSymptom,Medicine,MedicineDisease
from django.http import JsonResponse

def process_symptoms(request):
    if request.method == 'POST':
       ######for string
        # entered_symptoms = request.POST.get('symptoms', '')
        global entered_symptoms
        ########for list
        entered_symptoms = request.POST.get('symptoms', '').split(',')
        matched_diseases = get_matched_diseases(entered_symptoms)
        return render(request, 'w_disease12years.html', {'matched_diseases': matched_diseases})
    else:
        return render(request, 'index.html')

def get_matched_diseases(entered_symptoms):
    symptom_ids = Symptom.objects.filter(name__in=entered_symptoms).values_list('id', flat=True)
    matched_disease_ids = DiseaseSymptom.objects.filter(symptom_id__in=symptom_ids).values_list('disease_id', flat=True)

    total_symptoms_counts = DiseaseSymptom.objects.filter(disease_id__in=matched_disease_ids).values('disease_id').annotate(total_symptoms_count=Count('symptom'))
    matched_symptoms_counts = DiseaseSymptom.objects.filter(disease_id__in=matched_disease_ids, symptom_id__in=symptom_ids).values('disease_id').annotate(matched_symptoms_count=Count('symptom'))

    percentage_matches = {}
    for total_count in total_symptoms_counts:
        disease_id = total_count['disease_id']
        total_symptoms = total_count['total_symptoms_count']
        matched_count = next((match['matched_symptoms_count'] for match in matched_symptoms_counts if match['disease_id'] == disease_id), 0)
        match_percentage = (matched_count / total_symptoms) * 100 if total_symptoms != 0 else 0
        percentage_matches[disease_id] = match_percentage
    matched_diseases = Disease.objects.filter(id__in=matched_disease_ids)

    result = []
    for disease in matched_diseases:
        result.append({'disease': disease, 'percentage_match': percentage_matches.get(disease.id, 0)})

    return result


def treatment(request, disease_id):
    disease = get_object_or_404(Disease, pk=disease_id)
    medicines = MedicineDisease.objects.filter(disease=disease).select_related('medicine')
    return render(request, 'w_treatment12years.html', {'disease': disease, 'medicines': medicines})

def get_symptoms12years(request, disease_id):
    symptoms = Symptom.objects.filter(diseasesymptom__disease_id=disease_id)
    symptom_data = [{'name': symptom.name} for symptom in symptoms]
    return JsonResponse({'symptoms': symptom_data, 'entered_symptoms':entered_symptoms})

def get_suggestions12years(request):
    query = request.GET.get('query', '')
    suggestions = Symptom.objects.filter(name__icontains=query).values_list('name', flat=True)
    return JsonResponse(list(suggestions), safe=False)

