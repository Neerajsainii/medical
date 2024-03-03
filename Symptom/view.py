from django.shortcuts import render
from django.http import JsonResponse
from .models import Disease, Symptom, DiseaseSymptom
from django.db.models import Count, Q


def process_symptoms(request):
    if request.method == 'POST':
       ######for string
        # entered_symptoms = request.POST.get('symptoms', '')

        ########for list
        entered_symptoms = request.POST.get('symptoms', '').split(',')
        print("Entered Symptoms:", entered_symptoms)
        matched_diseases = get_matched_diseases(entered_symptoms)
        print(matched_diseases)
        return render(request, 'matchdisease.html', {'matched_diseases': matched_diseases})
    else:
        return render(request, 'index.html')

# def get_matched_diseases(entered_symptoms):
    ####for list
    # all_symptoms = Symptom.objects.filter(name=entered_symptoms[0]).values_list('name')
    # matched_disease_ids = DiseaseSymptom.objects.all().values_list('symptom_id')
    # print(matched_disease_ids)

    ###for string
    # symptomss_id = Symptom.objects.filter(name=entered_symptoms).values_list('id', flat=True).first()
    # print(symptomss_id)
    # matched_disease_ids = DiseaseSymptom.objects.filter(symptom_id=symptomss_id).values_list('disease_id')
    # print("Matched Disease IDs:", matched_disease_ids)
    # matched_diseases = Disease.objects.filter(id__in=matched_disease_ids)
  # For a list (multiple symptoms)
    symptom_ids = Symptom.objects.filter(name__in=entered_symptoms).values_list('id', flat=True)

    print("hari",symptom_ids)
    # You can uncomment the above line if entered_symptoms is a list

    matched_diseases = Disease.objects.filter(diseasesymptom__symptom_id=symptom_ids)
    # If using the list of symptom_ids, modify the line to:
    # matched_diseases = Disease.objects.filter(diseasesymptom__symptom_id__in=symptom_ids)


    print("Matched Diseases:", matched_diseases)
    return matched_diseases
# def get_matched_diseases(entered_symptoms):
    # Fetching symptom IDs
    symptom_ids = Symptom.objects.filter(name__in=entered_symptoms).values_list('id', flat=True)

    print("Symptom IDs:", symptom_ids)

    # Fetching matched diseases based on symptom IDs
    matched_diseases = Disease.objects.filter(diseasesymptom__symptom_id__in=symptom_ids).distinct()

    print("Matched Diseases:", matched_diseases)

    return matched_diseases
from django.db.models import Count

def get_matched_diseases(entered_symptoms):
    symptom_ids = Symptom.objects.filter(name__in=entered_symptoms).values_list('id', flat=True)
    
    # Query to retrieve diseases that match the entered symptoms
    matched_disease_ids = DiseaseSymptom.objects.filter(symptom_id__in=symptom_ids).values_list('disease_id', flat=True)

    # Count the number of matched symptoms for each disease
    symptom_counts = DiseaseSymptom.objects.filter(disease_id__in=matched_disease_ids).values('disease_id').annotate(count=Count('symptom'))

    # Calculate the percentage match for each disease
    percentage_matches = {}
    for symptom_count in symptom_counts:
        disease_id = symptom_count['disease_id']
        total_symptoms = DiseaseSymptom.objects.filter(disease_id=disease_id).count()
        match_percentage = (symptom_count['count'] / total_symptoms) * 100
        percentage_matches[disease_id] = match_percentage

    # Fetch Disease objects based on matched IDs
    matched_diseases = Disease.objects.filter(id__in=matched_disease_ids)

    # Combine disease information with percentage match
    result = []
    for disease in matched_diseases:
        result.append({'disease': disease, 'percentage_match': percentage_matches.get(disease.id, 0)})

    return result
def Home(request):


    return render(request,'index.html')
