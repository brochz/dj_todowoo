from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

# https://learning.oreilly.com/videos/django-3/9781801818148/9781801818148-video7_5/
# Create your views here.
def signupuser(request):
    if request.method == "GET":
        return render(request, "signupuser.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] ==  request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                #Login user after signup
                login(request, user)
                return redirect("currenttodos")
            except IntegrityError:
                return render(request, "signupuser.html", {"form": UserCreationForm(), "error": "Username already taken"})
        else:
            return render(request, "signupuser.html", {"form": UserCreationForm(), "error": "Passwords did not match"})


def currenttodos(request):
    return render(request, "currenttodos.html") 