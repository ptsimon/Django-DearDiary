from django.shortcuts import render, redirect
from .models import Entry
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    if request.method == "POST":
        data = request.POST['entry']
        new = Entry(content=data, user=request.user)
        new.save()

        return render(request, 'entries/home.html')
    else:
        return render(request, 'entries/home.html')

@login_required(login_url='/accounts/login')
def history(request):
    log_user = request.user
    user_entries = entries.objects.filter(user=log_user)
    return render(request, 'entries/history.html', {'entries': user_entries})