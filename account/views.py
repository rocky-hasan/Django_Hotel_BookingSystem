from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = authenticate(username=username, password=password)
        
        if user_obj is not None:
            login(request, user_obj)
            messages.success(request, 'Login successful')
            return redirect('hotel') 
        else:
            messages.warning(request, 'Invalid credentials')
    
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #  if the username already exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect('register')  # Redirect to the registration page

        # Here I Create a new user
        user = User.objects.create(username=username)
        user.set_password(password)  # Set the password using the entered password
        user.save()

        messages.success(request, 'Registration successful')
        return redirect('hotel') 

    return render(request, 'register.html')