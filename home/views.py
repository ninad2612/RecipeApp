from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Accounts
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if user exists
        if not User.objects.filter(username=username).exists() :
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)

        if user is None :
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        
        else :
            login(request,user)
            return redirect('/display_recipes/')      

    return render(request,'login.html')

def logout_page(request):

    logout(request)

    return redirect('/login/')

def register_page(request): 
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Taken")
            return redirect('/register/')  # Use return here to properly redirect

        # Create a new user
        user = User(
            username=username,
            first_name=firstname,
            last_name=lastname,
        )
        user.set_password(password)  # Use set_password to hash the password
        user.save()


        messages.success(request, "Account created successfully.")
        return redirect('/register/')  # Redirect to the login page after successful registration

    return render(request, 'register.html')

