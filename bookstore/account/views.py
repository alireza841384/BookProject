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
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, "mypages/signup.html", {"form": form})


def loginView(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'mypages/login.html', {'form': form})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_massage = "username or password is incorrect!"
            return render(request, 'mypages/login.html', {'error_message': error_massage})
