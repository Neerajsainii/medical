from django.http import HttpResponseRedirect
from django.urls import reverse

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Logic to check if the request is for a restricted URL
        restricted_urls = ["/info/", "/w/", "/wabout/", "/wemergency/", "/wsymptom/", "/wsymptoms/", "/wtreatment/", "/wdisease/", "/wprecaution/", "/winfant/", "/wchild/", "/wbmi/",
    "/get_suggestions2months/", "/symptom2months/", "/get_symptoms2months/<int:disease_id>/",
    "/disease2months/", "/medicine2months/<int:disease_id>/",
    "/get_suggestions5years/", "/symptom5years/", "/get_symptoms5years/<int:disease_id>/",
    "/disease5years/", "/medicine5years/<int:disease_id>/",
    "/get_suggestions12years/", "/symptom12years/", "/get_symptoms12years/<int:disease_id>/",
    "/disease12years/", "/medicine12years/<int:disease_id>/",
    "/get_suggestions18years/", "/symptom18years/", "/get_symptoms18years/<int:disease_id>/",
    "/disease18years/", "/medicine18years/<int:disease_id>/",
    "/get_suggestions65years/", "/symptom65years/",
    "/get_symptoms65years/<int:disease_id>/", "/disease65years/", "/medicine65years/<int:disease_id>/",
    "/get_suggestionsplusyears/",  "/symptomplusyears/", "/get_symptomsplusyears/<int:disease_id>/",
    "/diseaseplusyears/", "/medicineplusyears/<int:disease_id>/"
]

        if request.path_info in restricted_urls and not request.user.is_authenticated:
            # If the user is not authenticated, redirect to the login page
            return HttpResponseRedirect(reverse('userLogin'))  # Update to use 'userLogin' and specify the app name here

        # Allow the request to proceed to the view
        response = self.get_response(request)
        return response
