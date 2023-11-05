from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupuser(request):
    print(request.POST)
    return render(request, "signupuser.html", {"form": UserCreationForm()})