# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Disease, Symptom, DiseaseSymptom
# from .models import Disease, Symptom, DiseaseSymptom
# from django.shortcuts import render
# from django.http import JsonResponse


def process_symptoms(request):
    if request.method == 'POST':
        # Handle form submission and fetch matched diseases based on entered symptoms
        ######for string
        entered_symptoms = request.POST.get('symptoms', '')

        ########for list
        # entered_symptoms = request.POST.get('symptoms', '').split(',')
        print("Entered Symptoms:", entered_symptoms)
        matched_diseases = get_matched_diseases(entered_symptoms)
        print(matched_diseases)
        return render(request, 'matchdisease.html', {'matched_diseases': matched_diseases})
    # else:
    #     # Render the initial form
    #     return render(request, 'index.html')

def get_matched_diseases(entered_symptoms):
    ####for list
    # all_symptoms = Symptom.objects.filter(name=entered_symptoms[0]).values_list('name')
    
    # matched_disease_ids = DiseaseSymptom.objects.all().values_list('symptom_id')
    # print(matched_disease_ids)

    ###for string
    symptomss_id = Symptom.objects.filter(name=entered_symptoms).values_list('id', flat=True).first()
    print(symptomss_id)
    matched_disease_ids = DiseaseSymptom.objects.filter(symptom_id=symptomss_id).values_list('disease_id')
    print("Matched Disease IDs:", matched_disease_ids)

    # Fetch Disease objects based on matched IDs
    matched_diseases = Disease.objects.filter(id__in=matched_disease_ids)
    
    print("Matched Diseases:", matched_diseases)

    return matched_diseases

def Home(request):


    return render(request,'index.html')
# views.py

# def create_disease_symptoms(request):
#     disease_symptoms_dict = {
#         "Acne": ["Pimples", "Blackheads", "Whiteheads", "Oily skin"],
#         "Allergies": ["Sneezing", "Runny nose", "Watery eyes", "Itchy throat"],
#         "Anemia": ["Fatigue", "Weakness", "Pale skin", "Shortness of breath"],
#         "Anxiety disorders": ["Excessive worrying", "Restlessness", "Fatigue", "Difficulty concentrating"],
#         "Asthma": ["Shortness of breath", "Coughing", "Wheezing", "Chest tightness"],
#         "Back pain": ["Lower back pain", "Muscle stiffness", "Difficulty standing upright", "Radiating pain"],
#         "Bronchitis": ["Cough", "Mucus production", "Chest discomfort", "Fatigue"],
#         "Cancer": ["Unexplained weight loss", "Fatigue", "Lump or mass", "Changes in bowel or bladder habits"],
#         "Celiac disease": ["Abdominal pain", "Bloating", "Diarrhea", "Fatigue"],
#         "Chronic fatigue syndrome": ["Fatigue", "Muscle or joint pain", "Headaches", "Memory problems"],
#         "Chronic obstructive pulmonary disease (COPD)": ["Shortness of breath", "Wheezing", "Chronic cough", "Chest tightness"],
#         "Common cold": ["Runny or stuffy nose", "Sneezing", "Sore throat", "Cough"],
#         "Diabetes mellitus": ["Increased thirst", "Frequent urination", "Fatigue", "Blurry vision"],
#         "Fibromyalgia": ["Widespread pain", "Fatigue", "Sleep disturbances", "Difficulty concentrating"],
#         "Gastroesophageal reflux disease (GERD)": ["Heartburn", "Regurgitation", "Difficulty    swallowing", "Chest pain"],
#         "Heart disease": ["Chest pain", "Shortness of breath", "Fatigue", "Dizziness or lightheadedness"],
#         "Hypertension": ["High blood pressure", "Headaches", "Chest pain", "Fatigue"],
#         "Inflammatory bowel disease (IBD)": ["Abdominal pain", "Diarrhea", "Rectal bleeding", "Weight loss"],
#         "Irritable bowel syndrome (IBS)": ["Abdominal pain", "Bloating", "Gas", "Diarrhea or    constipation"],
#         "Kidney disease": ["Fatigue", "Swelling in legs, ankles, or feet", "Foamy urine", "Changes in urination frequency"],
#         "Lupus": ["Fatigue", "Joint pain", "Butterfly-shaped rash", "Fever"],
#         "Migraine": ["Intense headaches", "Nausea", "Sensitivity to light or sound", "Visual    disturbances"],
#         "Multiple sclerosis": ["Fatigue", "Difficulty walking", "Numbness or weakness", "Tingling or pain"],
#         "Obesity": ["Increased body weight", "Fatigue", "Shortness of breath", "Joint pain"],
#         "Osteoarthritis": ["Joint pain", "Stiffness", "Swelling", "Decreased range of motion"],
#         "Osteoporosis": ["Fractures", "Back pain", "Loss of height", "Hunched posture"],
#         "Parkinson's disease": ["Tremors", "Slowed movement", "Stiff muscles", "Impaired posture and balance"],
#         "Rheumatoid arthritis": ["Joint pain", "Swelling", "Stiffness", "Fatigue"],
#         "Schizophrenia": ["Hallucinations", "Delusions", "Disorganized thinking", "Lack of motivation"],
#         "Stroke": ["Weakness or numbness", "Difficulty speaking", "Confusion", "Trouble walking"]
#     }
#     for disease_name, symptom_names in disease_symptoms_dict.items():
#         disease, created_disease = Disease.objects.get_or_create(name=disease_name)
#         symptoms = [Symptom.objects.get_or_create(name=symptom_name)[0] for symptom_name in symptom_names]

#         for symptom in symptoms:
#             DiseaseSymptom.objects.get_or_create(disease=disease, symptom=symptom)

#     return JsonResponse({'message': 'Successfully created DiseaseSymptom entries'})
