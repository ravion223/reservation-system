from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CustomUserCreationForm


# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
        
    else:
        form = CustomUserCreationForm()
    
    return render(
        request,
        "auth_system/register-form.html",
        {"form": form}
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error("Wrong password or username")

        
    else:
        form = AuthenticationForm()

    return render(
        request,
        "auth_system/login-form.html",
        {"form":form}
    )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')