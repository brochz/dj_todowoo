from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Todo
from django.contrib.auth.decorators import login_required
# https://learning.oreilly.com/videos/django-3/9781801818148/9781801818148-video7_12/
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
    todos = Todo.objects.filter(user=request.user, datacompleted__isnull=True)
    return render(request, "currenttodos.html", {"todos": todos})


def completetodos(request):
    todos = Todo.objects.filter(user=request.user, datacompleted__isnull=False).order_by("-datacompleted")
    return render(request, "completetodos.html", {"todos": todos})





def logoutuser(request):
    if request.method == "POST":
        logout(request)

    return redirect("home")


def loginuser(request):
    if request.method == "GET":
        return render(request, "loginuser.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "loginuser.html", {"form": AuthenticationForm(), "error": "Username and password did not match"})
        else:
            login(request, user)
            return redirect("currenttodos")


from .forms import TodoForm


@login_required
def createtodo(request):
    """
    View function that handles creation of a new todo item.

    If the request method is GET, it renders the createtodo.html template with an empty TodoForm.
    If the request method is POST, it validates the form data and saves the new todo item to the database.

    Returns:
        If the request method is GET, it returns a rendered HTML template.
        If the request method is POST and the form data is valid, it redirects to the currenttodos view.
        If the request method is POST and the form data is invalid, it returns a rendered HTML template with an error message.
    """
    if request.method == "GET":
        # Render the createtodo.html template with an empty TodoForm
        return render(request, "createtodo.html", {"form": TodoForm()})
    else:

        try:
 
            # Validate the form data
            form = TodoForm(request.POST)


            # Save the form to  the database
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            # Redirect to the currenttodos view
            return redirect("currenttodos")
        except ValueError as e:
            # Return a rendered HTML template with an error message
            return render(request, "createtodo.html", {"form": TodoForm(), "error": "Bad data passed in. Try again."})  

def home(request):
    return render(request, "home.html")

def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "GET":
        form = TodoForm(instance=todo)
        return render(request, "viewtodo.html", {"todo": todo, "form": form})    
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return  redirect("viewtodo", todo_pk=todo_pk)    
        except ValueError:
            return render(request, "viewtodo.html", {"todo": todo, "form": form, "error": "Bad info"})
        

def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.datacompleted = timezone.now()
        todo.save()
        return redirect("currenttodos")
    

def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect("currenttodos")