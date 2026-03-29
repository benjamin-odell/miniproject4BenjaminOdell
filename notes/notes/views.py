from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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


