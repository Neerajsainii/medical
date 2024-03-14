from django.contrib import admin
from django.urls import path
from Symptom import view
from Medicine import viewss
from Signup import views
from Home import vieew


urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.userSignup, name="userSignup"),
    path("login/", views.userLogin,name="userLogin"),
    path("contac/", views.contact,name="contact"),
    path("", vieew.home ),
    path("", views.home ,name="home"),
    path("about/", vieew.about),
    path("emergency/", vieew.emergency),
    path("symptom/", vieew.Symptom),
    path("contact/", vieew.contact ),
    path("infant/", vieew.infant),
    path("child/", vieew.child), 
     path("treatment/", vieew.treatment),
       path("disease/", vieew.disease),
    path('get_symptoms/<int:disease_id>/', view.get_symptoms, name='get_symptoms'),
    path('get_suggestions/', view.get_suggestions, name='get_suggestions'),
    path("info/", vieew.info),
    path('/', view.process_symptoms, name='process_symptoms'), 
    path('disease_medicines/<int:disease_id>/', viewss.treatment, name='disease_medicines'),
]