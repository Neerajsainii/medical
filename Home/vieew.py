from django.shortcuts import render
def custom_404(request, exception=None):
    return render(request,'404.html', status=404)
def home(request):
    return render(request,'index.html')

def about(request):
    return render (request,'about.html')

def emergency(request):
    return render (request,'emergency.html')

def Symptom(request):
    return render(request,'symptom.html')

def symptoms(request):
    return render(request,'symptoms.html')

def symptom2months(request):
    return render(request,'w_symptom2months.html ')
def symptom5years(request):
    return render(request,'w_symptom5years.html ')
def symptom12years(request):
    return render(request,'w_symptom12years.html ')
def symptom18years(request):
    return render(request,'w_symptom18years.html ')
def symptom65years(request):
    return render(request,'w_symptom65years.html ')
def symptomplusyears(request):
    return render(request,'w_symptomplusyears.html ')

    

def contact(request):
    return render(request,'contact.html ')


def infant(request):
    return render(request,'infant.html ')

def child(request):
    return render(request,'child.html ')


def login(request):
    return render(request,'login.html')
def info(request):
    return render(request,'info.html ')
def bmi(request):
    return render(request,'bmi.html ')



def whome(request):
    return render(request,'w_index.html')

def wcontact(request):
    return render(request,'w_contact.html ')

def wabout(request):
    return render (request,'w_about.html')

def wemergency(request):
    return render (request,'w_emergency.html')

def wSymptom(request):
    return render(request,'w_symptom.html')

def wsymptoms(request):
    return render(request,'w_symptoms.html') 

def wtreatment(request):
    return render(request,'w_treatment.html ')

def wdisease(request):
    return render(request,'w_disease.html ')
def wprecaution(request):
    return render(request,'w_precaution.html')   

def winfant(request):
    return render(request,'w_infant.html ')

def wchild(request):
    return render(request,'w_child.html ')

def wbmi(request):
    return render(request,'w_bmi.html ')        



# def infoage(request):
#     if request.method == 'POST':
#         age = request.POST.get('age')

#         if age:
#             if int(age) >=0 and int(age) <= 5:
#                 return render(request, 'w_symptom5years.html')
#             elif int(age) > 5 and int(age) <=12 :
#                 return render(request, 'w_symptom12years.html')
#             elif int(age) > 12 and int(age) <=18 :
#                 return render(request, 'w_symptom12years.html')
#             elif int(age) > 18 and int(age) <=65 :
#                 return render(request, 'w_symptom65years.html')
#             elif int(age) > 65 and int(age) <=100 :
#                 return render(request, 'w_symptomplusyears.html')
#             else:
#                 return render(request,'info.html')

#     return render(request, 'w_index.html')

def treatment(request):
    return render(request,'treatment.html ')

def disease(request):
    return render(request,'disease.html ')
def precaution(request):
    return render(request,'precaution.html ')


# ////with login section
