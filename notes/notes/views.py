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
    if request.method == "POST":
        #create user
        pass
    else:
        #render page
        return render(request, 'notes/create_user.html')

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


