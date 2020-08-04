from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from entries.views import home

# Create your views here.
def login(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request, 'accounts/login.html', {'error': "Invalid login credentials."})
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['retypepassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/register.html', {'error': "Username Taken."})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'] 
                )
                # return render(request, 'accounts/login.html', {'error': "Account created. Please Login."})
            return redirect(login)
        else:
            return render(request, 'accounts/register.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    auth.logout(request)
    return redirect(login)