# urls.py

from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from Signup import views as signup_views
from Home import vieew as home_views
from agezeroto2months import views2months
from age2to5years import views5years
from age5to12years import views12years
from age12to18years import views18years
from age18two65years import views65years
from age65toplusyears import viewsplusyears
from django.conf.urls import handler404  
urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", signup_views.userSignup, name="userSignup"),
    path("login/", signup_views.userLogin, name="userLogin"),
    path("contact/", signup_views.contact, name="contact"),
    path("", home_views.home, name="home"),
    path("404/", home_views.custom_404),
    path("about/", home_views.about, name="about"),
    path("emergency/", home_views.emergency, name="emergency"),
    path("symptom/", home_views.Symptom, name="symptom"),
    path("infant/", home_views.infant, name="infant"),
    path("child/", home_views.child, name="child"),
    path("bmi/", home_views.bmi, name="bmi"),
    path("precaution/", home_views.precaution, name="precaution"),
    path("treatment/", home_views.treatment, name="treatment"),
    path("disease/", home_views.disease, name="disease"),
    # Add your restricted URLs here with login_required decorator
    path("info/", login_required(home_views.info), name="info"),
    path("w/", login_required(home_views.whome), name="whome"),
    path("wabout/", login_required(home_views.wabout), name="wabout"),
    path("wemergency/", login_required(home_views.wemergency), name="wemergency"),
    path("wsymptom/", login_required(home_views.wSymptom), name="wsymptom"),
    path("wsymptoms/", login_required(home_views.wsymptoms), name="wsymptoms"),
    path("wtreatment/", login_required(home_views.wtreatment), name="wtreatment"),
    path("wdisease/", login_required(home_views.wdisease), name="wdisease"),
    path("wprecaution/", login_required(home_views.wprecaution), name="wprecaution"),
    path("winfant/", login_required(home_views.winfant), name="winfant"),
    path("wchild/", login_required(home_views.wchild), name="wchild"),
    path("wbmi/", login_required(home_views.wbmi), name="wbmi"),
   
   # ///zero to 2 months
    path('get_suggestions2months/', views2months.get_suggestions2months,name='get_suggestions2months'), 
    path('symptom2months/', home_views.symptom2months),
    path('get_symptoms2months/<int:disease_id>/', views2months.get_symptoms2months,name='get_symptoms2months'),
    path('disease2months/', views2months.process_symptoms, name='disease2months'), 
    path('medicine2months/<int:disease_id>/', views2months.treatment, name='medicine2months'),

    # ///2 months to 5 years 
    path('get_suggestions5years/', views5years.get_suggestions5years,name='get_suggestions5years'),
    path('/', views5years.process_symptoms, name='symptoms5years'), 
    path('symptom5years/', home_views.symptom5years),
     path('get_symptoms5years/<int:disease_id>/', views5years.get_symptoms5years,name='get_symptoms5years'),
      path('disease5years/', views5years.process_symptoms, name='disease5years'),
    path('medicine5years/<int:disease_id>/', views5years.treatment, name='medicine5years'),

    # ///5 to 12 years 
    path('get_suggestions12years/', views12years.get_suggestions12years,name='get_suggestions12years'),
    path('/', views12years.process_symptoms, name='symptoms12years'), 
    path('symptom12years/', home_views.symptom12years),
    path('get_symptoms12years/<int:disease_id>/', views12years.get_symptoms12years,name='get_symptoms12years'),
      path('disease12years/', views12years.process_symptoms, name='disease12years'),
    path('medicine12years/<int:disease_id>/', views12years.treatment, name='medicine12years'),

    # ///12 to 18 years 
    path('get_suggestions18years/', views18years.get_suggestions18years,name='get_suggestions18years'),
    path('/', views18years.process_symptoms, name='symptoms18years'), 
    path('symptom18years/', home_views.symptom18years),
     path('get_symptoms18years/<int:disease_id>/', views18years.get_symptoms18years,name='get_symptoms18years'),
      path('disease18years/', views18years.process_symptoms, name='disease18years'),
    path('medicine18years/<int:disease_id>/', views18years.treatment, name='medicine18years'),

    # ///18 to 65 years 
    path('get_suggestions65years/', views65years.get_suggestions65years,name='get_suggestions65years'),
    path('get_suggestions/', views65years.get_suggestions, name='get_suggestions'),
    path('symptom65years/', home_views.symptom65years),
     path('get_symptoms65years/<int:disease_id>/', views65years.get_symptoms65years,name='get_symptoms65years'),
      path('disease65years/', views65years.process_symptoms, name='disease65years'),
    path('get_symptoms/<int:disease_id>/', views65years.get_symptoms, name='get_symptoms'),
    path('disease/', views65years.process_symptoms, name='process_symptoms'), 
    path('medicine65years/<int:disease_id>/', views65years.treatment, name='medicine65years'),
    
    # ///65 to plus years
    path('get_suggestionsplusyears/', viewsplusyears.get_suggestionsplusyears,name='get_suggestionsplusyears'),
    path('/', viewsplusyears.process_symptoms, name='symptomsplus'), 
    path('symptomplusyears/', home_views.symptomplusyears),
     path('get_symptomsplusyears/<int:disease_id>/', viewsplusyears.get_symptomsplusyears,name='get_symptomsplusyears'),
      path('diseaseplusyears/', viewsplusyears.process_symptoms, name='diseaseplusyears'),
    path('medicineplusyears/<int:disease_id>/', viewsplusyears.treatment, name='medicineplusyears'),

]
handler404 = 'Home.vieew.custom_404'