from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login as auth_login
from .forms import MyCustomSignupForm


from .models import *

#Landing Screen
def index(request):
    return render(request, 'core/index.html', {
        # Data to return to template
    })

#Home Screen
def home(request):
    return render(request, 'core/home.html', {
        # Data to return to template
    })

def signup(response):
    if response.method == "POST":
        form = MyCustomSignupForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = MyCustomSignupForm()
    return render(response, "registration/accounts/signup/", {"form":form})