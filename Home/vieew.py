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


def contact(request):
    return render(request,'contact.html ')
