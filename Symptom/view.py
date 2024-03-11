from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .models import Disease, Symptom , DiseaseSymptom

def process_symptoms(request):
    if request.method == 'POST':
       ######for string
        # entered_symptoms = request.POST.get('symptoms', '')

        ########for list
        entered_symptoms = request.POST.get('symptoms', '').split(',')
        # print("Entered Symptoms:", entered_symptoms)
        matched_diseases = get_matched_diseases(entered_symptoms)
        # print(matched_diseases)
        return render(request, 'disease.html', {'matched_diseases': matched_diseases})
    else:
        return render(request, 'index.html')

def get_matched_diseases(entered_symptoms):
    symptom_ids = Symptom.objects.filter(name__in=entered_symptoms).values_list('id', flat=True)
   
    matched_disease_ids = DiseaseSymptom.objects.filter(symptom_id__in=symptom_ids).values_list('disease_id', flat=True)

    symptom_counts = DiseaseSymptom.objects.filter(disease_id__in=matched_disease_ids).values('disease_id').annotate(count=Count('symptom'))
    # print("Symptom Counts:", symptom_counts[0])

    percentage_matches = {}
    for symptom_count in symptom_counts:
        disease_id = symptom_count['disease_id']
        total_symptoms = DiseaseSymptom.objects.filter(disease_id=disease_id).count()
        match_percentage = (symptom_count['count'] / total_symptoms) * 100
        print(f"Disease ID: {disease_id}, Total Symptoms: {total_symptoms}, Match Percentage: {match_percentage}")
        percentage_matches[disease_id] = match_percentage

    matched_diseases = Disease.objects.filter(id__in=matched_disease_ids)

    result = []
    for disease in matched_diseases:
        result.append({'disease': disease, 'percentage_match': percentage_matches.get(disease.id, 0)})

    return result



