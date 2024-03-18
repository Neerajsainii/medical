from django.shortcuts import render

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

def contact(request):
    return render(request,'contact.html ')


def infant(request):
    return render(request,'infant.html ')

def child(request):
    return render(request,'child.html ')

def info(request):
    return render(request,'info.html ')


def infoage(request):
    if request.method == 'POST':
        age = request.POST.get('age')

        if age:
            if int(age) >=0 and int(age) <= 5:
                return render(request, 'w_symptom5years.html')
            elif int(age) > 5 and int(age) <=12 :
                return render(request, 'w_symptom12years.html')
            elif int(age) > 12 and int(age) <=18 :
                return render(request, 'w_symptom12years.html')
            elif int(age) > 18 and int(age) <=65 :
                return render(request, 'w_symptom65years.html')
            elif int(age) > 65 and int(age) <=100 :
                return render(request, 'w_symptomplusyears.html')
            else:
                return render(request,'info.html')

    return render(request, 'w_index.html')

def treatment(request):
    return render(request,'treatment.html ')

def disease(request):
    return render(request,'disease.html ')
def precaution(request):
    return render(request,'precaution.html ')

# ////with login section
# def wSymptom0to2(request):
#     return render(request,'w_symptom2months.html ')
