from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {"user": request.user}
    return render(request, "mypages/home.html")


# account/views.py

import random
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect


def signupView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # ایمیل را بگیر
            email = form.cleaned_data['email']
            
            # کد ۶ رقمی بساز
            code = str(random.randint(100000, 999999))

            # ذخیره اطلاعات توی session
            request.session['temp_user_data'] = {
                'username': form.cleaned_data['username'],
                'email': email,
                'password1': form.cleaned_data['password1'],
                'password2': form.cleaned_data['password2'],
                'code': code
            }

            # ارسال ایمیل
            send_mail(
                'Verification Code',
                f'Your verification code is: {code}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return redirect('verify_email')
    else:
        form = CustomUserCreationForm()

    return render(request, "mypages/signup.html", {"form": form})


def verify_email(request):
    error = ""
    data = request.session.get('temp_user_data')

    if not data:
        return redirect('signup')

    if request.method == "POST":
        input_code = request.POST.get("code")

        if input_code == data['code']:
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password1']
            )
            login(request, user)

            if 'temp_user_data' in request.session:
                del request.session['temp_user_data']

            return redirect('home')
        else:
            error = "Incorrect verification code."

    return render(request, "mypages/verify_code.html", {"error": error})


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
