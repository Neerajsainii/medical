from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def symptomHome(request):
    return render(request,'symptom_checker.html')