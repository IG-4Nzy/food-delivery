from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models  import  Person
from datetime import date, datetime
from django.core.mail import send_mail


def log_sin(request):
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('user_password')
        email = request.POST.get('email')
        
        # Check if a user with the same username already exists
        if Person.objects.filter(uname=uname).exists():
            return render(request, 'signup.html', {'error_message': 'User already exists'})
        
        person = Person(uname=uname, pass1=pass1, email=email)
        person.save()
        
        # Redirect to a success page or render a template
        return render(request, 'home.html')
    
    return render(request, 'signup.html')