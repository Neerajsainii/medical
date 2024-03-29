from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from .models import UserSignup,Contact

def userSignup(request):
    if request.method == 'POST':
        user_data = {
            'firstname': request.POST.get('firstname'),
            'lastname': request.POST.get('lastname'),
            'age': request.POST.get('age'),
            'gender': request.POST.get('gender'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'repassword': request.POST.get('repassword'),
        }
        if UserSignup.objects.filter(email=user_data['email']).exists():
            return HttpResponse('User with this email already exists. Please choose a different one.')

        if user_data['password'] != user_data['repassword']:
            return HttpResponse('Passwords do not match. Please try again.')

        hashed_password = make_password(user_data['password'])

        user = UserSignup(
            firstname=user_data['firstname'],
            lastname=user_data['lastname'],
            age=user_data['age'],
            gender=user_data['gender'],
            email=user_data['email'],
            password=hashed_password,
        )
        user.save()
        print('User signed up successfully!')

        return redirect('whome') 

    return render(request, 'signup.html')


def userLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        # print(password)
        user = authenticate(request, email=email, password=password)
        # print(user.check_password)

        if user is not None:
            login(request, user)
            return redirect('whome')
        else:
            return HttpResponse('Invalid login credentials. Please try again.')

    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('home')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Contact object
        contact = Contact.objects.create(
            full_name=full_name,
            email=email,
            message=message
        )
        
        # Optionally, you can perform additional validations here
        
        # Save the Contact object
        contact.save()

        return redirect('whome')  # Redirect to the same page after form submission
    
    return render(request, 'contact.html')

def home(request):
    return render(request,'index.html')
