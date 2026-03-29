from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "notes/index.html")

@login_required
def note(request):
    return

def create_user(request):
    error = None
    if request.method == "POST":
        #create user

        #check for username and password
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is None:
            error = "Username is required."
        elif password is None:
            error = "Password is required."
        else:
            #check for user
            user = User.objects.filter(username=username)
            if user:
                error = "Username already exists."
            else:
                User.objects.create_user(username=username, password=password)
                return HttpResponseRedirect(reverse("login"))

    #render page
    return render(request, 'notes/create_user.html', {"error": error})

@login_required
def logout_view (request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def login_view (request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username is None:
            error = "Username is required."
        elif password is None:
            error = "Password is required."

        else:

            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                error = "Incorrect username or password."

    return render(request, 'notes/login.html', {"error": error})


