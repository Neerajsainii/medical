from django.contrib import admin
from django.urls import path
from Signup import views
from Home import vieew
from agezeroto2months import views2months
from age2to5years import views5years
from age5to12years import views12years
from age12to18years import views18years
from age18to65years import views65years
from age65toplusyears import viewsplus

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
    path('/', views2months.process_symptoms, name='symptoms2months'), 
    path('medicine/<int:disease_id>/', views2months.treatment, name='medicine2months'),

    # ///2 months to 5 years 
    path('/', views5years.process_symptoms, name='symptoms5years'), 
    path('medicine/<int:disease_id>/', views5years.treatment, name='medicine5years'),

    # ///5 to 12 years 
    path('/', views12years.process_symptoms, name='symptoms12years'), 
    path('medicine/<int:disease_id>/', views12years.treatment, name='medicine12years'),

    # ///12 to 18 years 
    path('/', views18years.process_symptoms, name='symptoms18years'), 
    path('medicine/<int:disease_id>/', views18years.treatment, name='medicine18years'),

    # ///18 to 65 years 
    path('get_suggestions/', views65years.get_suggestions, name='get_suggestions'),
    path('get_symptoms/<int:disease_id>/', views65years.get_symptoms, name='get_symptoms'),
    path('/', views65years.process_symptoms, name='process_symptoms'), 
    path('medicines/<int:disease_id>/', views65years.treatment, name='medicines'),
    
    # ///65 to plus years
    path('/', viewsplus.process_symptoms, name='symptomsplus'), 
    path('medicine/<int:disease_id>/', viewsplus.treatment, name='medicineplus'),

    # path("w_symptom2months/", vieew.wSymptom0to2,name="zerototwomonths_symptoms"),
]