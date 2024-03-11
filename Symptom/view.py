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
    # Filter symptoms by those entered
    symptom_ids = Symptom.objects.filter(name__in=entered_symptoms).values_list('id', flat=True)

    # Get disease ids matching the entered symptoms
    matched_disease_ids = DiseaseSymptom.objects.filter(symptom_id__in=symptom_ids).values_list('disease_id', flat=True)

    # Count the total number of symptoms for each disease
    total_symptoms_counts = DiseaseSymptom.objects.filter(disease_id__in=matched_disease_ids).values('disease_id').annotate(total_symptoms_count=Count('symptom'))

    # Count the matched symptoms for each disease
    matched_symptoms_counts = DiseaseSymptom.objects.filter(disease_id__in=matched_disease_ids, symptom_id__in=symptom_ids).values('disease_id').annotate(matched_symptoms_count=Count('symptom'))

    percentage_matches = {}
    for total_count in total_symptoms_counts:
        disease_id = total_count['disease_id']
        total_symptoms = total_count['total_symptoms_count']
        
        # Get the matched symptoms count for the current disease
        matched_count = next((match['matched_symptoms_count'] for match in matched_symptoms_counts if match['disease_id'] == disease_id), 0)

        # Calculate match percentage
        match_percentage = (matched_count / total_symptoms) * 100 if total_symptoms != 0 else 0
        percentage_matches[disease_id] = match_percentage

    # Fetch matched diseases and their match percentages
    matched_diseases = Disease.objects.filter(id__in=matched_disease_ids)

    result = []
    for disease in matched_diseases:
        result.append({'disease': disease, 'percentage_match': percentage_matches.get(disease.id, 0)})

    return result

def process_disease(request, disease_id=None):
    if request.method == 'POST':
        # If it's a POST request, process the form data
        disease_name = request.POST.get('disease')
        matched_disease = Disease.objects.filter(name__icontains=disease_name).first()
        
        if matched_disease:
            symptoms = Symptom.objects.filter(diseasesymptom__disease=matched_disease)
            return render(request, 'disease_symptoms.html', {'disease': matched_disease, 'symptoms': symptoms})
        else:
            return render(request, 'no_matching_disease.html')
    else:
        # If it's not a POST request, check if a disease ID is provided
        if disease_id is not None:
            disease = get_object_or_404(Disease, pk=disease_id)
            symptoms = Symptom.objects.filter(diseasesymptom__disease=disease)
            return render(request, 'disease_symptoms.html', {'disease': disease, 'symptoms': symptoms})
        else:
            # If no disease ID is provided, render the default form
            return render(request, 'disease_form.html')