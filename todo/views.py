from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# https://learning.oreilly.com/videos/django-3/9781801818148/9781801818148-video7_4/
# Create your views here.
def signupuser(request):
    if request.method == "GET":
        return render(request, "signupuser.html", {"form": UserCreationForm()})
    else:
        User.objects.create_user(request.POST["username"], password=request.POST["password1"])