from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "mypages/home.html")


def signupView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home/')
    else:
        form = UserCreationForm()
    return render(request, "mypages/signup.html", {"form": form})


def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Incorrect username or password."
            return render(request, 'mypages/login.html', {
                'error_message': error_message,
                'username': username,
            })
    else:
        return render(request, 'mypages/login.html')
