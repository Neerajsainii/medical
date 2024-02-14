from django.contrib import admin

# Register your models here.
from .models import UserSignup

admin.site.register(UserSignup)