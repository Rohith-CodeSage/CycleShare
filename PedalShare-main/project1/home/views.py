from django.shortcuts import render, HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import User

def base(request):
    return render(request, 'frontend.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
     return render(request, 'contactus.html')

def availablecycles(request):
     return render(request, 'availablecycles.html') 

def contact(request):
    return HttpResponse("this is about page contact us")

def frontend(request):
    return render(request, 'frontend.html') 

def wallet(request):
    return render(request, 'wallet.html')

def PaymentGateway(request):
    return render(request, 'PaymentGateway.html')

def addabicycle(request):
    return render(request, 'addabicycle.html')

def changedestination(request):
    return render(request, 'changedestination.html')

def viewtransactions(request):
    return render(request, 'viewtransactions.html')

def previousbookings(request):
    return render(request, 'previousbookings.html')


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validation
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'signup.html')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')

        # Create new user
        try:
            user = User.objects.create_user(
                username=email,  # Using email as username
                email=email,
                password=password1
            )
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Replace 'home' with your home page URL name
        except Exception as e:
            messages.error(request, 'Error creating account')
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')  # Replace 'home' with your home page URL name
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'signin.html')
