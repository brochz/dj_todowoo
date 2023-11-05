from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# https://learning.oreilly.com/videos/django-3/9781801818148/9781801818148-video7_4/
# Create your views here.
def signupuser(request):
    print(request.POST)
    return render(request, "signupuser.html", {"form": UserCreationForm()})