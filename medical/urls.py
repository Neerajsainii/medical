from django.contrib import admin
from django.urls import path
from Signup import views
from Home import vieew
from agezeroto2months import views2months
from age2to5years import views5years
from age5to12years import views12years
from age12to18years import views18years
from age18two65years import views65years
from age65toplusyears import viewsplusyears

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.userSignup, name="userSignup"),
    path("login/", views.userLogin,name="userLogin"),
    path("contac/", views.contact,name="contact"),
    # ///without login section
    path("", vieew.home ),
    path("", views.home ,name="home"),
    path("about/", vieew.about),
    path("emergency/", vieew.emergency),
    path("symptom/", vieew.Symptom),
    path("contact/", vieew.contact ),
    path("infant/", vieew.infant),
    path("child/", vieew.child), 
    path("info/", vieew.info),
    path("precaution/", vieew.precaution),
    path("treatment/", vieew.treatment),
    path("disease/", vieew.disease),
    # ///with login
    path("/infoage", vieew.infoage,name="age"),
    # ///zero to 2 months
    path('get_suggestions2months/', views2months.get_suggestions2months,name='get_suggestions2months'), 
    path('symptom2months/', vieew.symptom2months),
    path('get_symptoms2months/<int:disease_id>/', views2months.get_symptoms2months,name='get_symptoms2months'),
    path('disease2months/', views2months.process_symptoms, name='disease2months'), 
    path('medicine/<int:disease_id>/', views2months.treatment, name='medicine2months'),

    # ///2 months to 5 years 
    path('/', views5years.process_symptoms, name='symptoms5years'), 
    path('symptom5years/', vieew.symptom5years),
      path('disease5years/', views5years.process_symptoms, name='disease5years'),
    path('medicine/<int:disease_id>/', views5years.treatment, name='medicine5years'),

    # ///5 to 12 years 
    path('/', views12years.process_symptoms, name='symptoms12years'), 
    path('symptom12years/', vieew.symptom12years),
      path('disease12years/', views12years.process_symptoms, name='disease12years'),
    path('medicine/<int:disease_id>/', views12years.treatment, name='medicine12years'),

    # ///12 to 18 years 
    path('/', views18years.process_symptoms, name='symptoms18years'), 
    path('symptom18years/', vieew.symptom18years),
      path('disease18years/', views18years.process_symptoms, name='disease18years'),
    path('medicine/<int:disease_id>/', views18years.treatment, name='medicine18years'),

    # ///18 to 65 years 
    path('get_suggestions/', views65years.get_suggestions, name='get_suggestions'),
    path('symptom65years/', vieew.symptom65years),
      path('disease65years/', views65years.process_symptoms, name='disease65years'),
    path('get_symptoms/<int:disease_id>/', views65years.get_symptoms, name='get_symptoms'),
    # path('d65years/', views65years.process_symptoms, name='process_symptoms'), 
    path('medicines/<int:disease_id>/', views65years.treatment, name='medicine65years'),
    
    # ///65 to plus years
    path('/', viewsplusyears.process_symptoms, name='symptomsplus'), 
    path('symptomplusyears/', vieew.symptomplusyears),
      path('diseaseplusyears/', viewsplusyears.process_symptoms, name='diseaseplusyears'),
    path('medicine/<int:disease_id>/', viewsplusyears.treatment, name='medicineplus'),

    # path("w_symptom2months/", vieew.wSymptom0to2,name="zerototwomonths_symptoms"),
]