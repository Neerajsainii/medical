from django.shortcuts import render

def Home(request):
    return render(request,'index.html')

def symptoms(request):
    return render(request,'symptoms.html')

def about(request):
    return render (request,'about.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html ')
