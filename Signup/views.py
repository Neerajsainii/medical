from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from .models import UserSignup

def userSignup(request):
    if request.method == 'POST':
        # Handle form submission logic here
        user_data = {
            'firstname': request.POST.get('firstname'),
            'lastname': request.POST.get('lastname'),
            'age': request.POST.get('age'),
            'gender': request.POST.get('gender'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'repassword': request.POST.get('repassword'),
        }

        # Check if a user with the same email already exists
        if UserSignup.objects.filter(email=user_data['email']).exists():
            return HttpResponse('User with this email already exists. Please choose a different one.')

        # Check if password and repassword match
        if user_data['password'] != user_data['repassword']:
            return HttpResponse('Passwords do not match. Please try again.')

        # Hash the password before saving to the database
        hashed_password = make_password(user_data['password'])

        # Save data to the database using the model
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

        # Redirect to a success page or home page
        return redirect('Home')  # 'Home' is the name of your home URL pattern

    return render(request, 'signup.html')


def userLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            return HttpResponse('Invalid login credentials. Please try again.')

    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('Home')

def Home(request):
    return render(request,'index.html')
