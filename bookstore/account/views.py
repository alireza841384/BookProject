from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm
from django.conf import settings
from django.core.mail import send_mail
import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import ProfileUser


@login_required
def home(request):
    context = {"user": request.user}
    return render(request, "mypages/home.html")


# account/views.py


def signupView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']

            code = str(random.randint(100000, 999999))

            request.session['temp_user_data'] = {
                'username': form.cleaned_data['username'],
                'email': email,
                'password1': form.cleaned_data['password1'],
                'password2': form.cleaned_data['password2'],
                'code': code
            }

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


def generate_code():
    return str(random.randint(100000, 999999))


def forgot_password_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'mypages/forgot_password.html', {'error': 'Username not found.'})
        if user.email != email:
            return render(request, 'mypages/forgot_password.html', {'error': 'Email does not match.'})
        code = generate_code()
        request.session['reset_user'] = user.username
        request.session['reset_code'] = code
        send_mail(
            subject='BookManagement Password Reset Code',
            message=f'Your password reset code is: {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        )

        return redirect('verify_forgot_code')
    return render(request, 'mypages/forgot_password.html')


def verify_forgot_code_view(request):
    if request.method == 'POST':
        code = request.POST['code']
        if code == request.session.get('reset_code'):
            return redirect('reset_password')
        return render(request, 'mypages/forgot_verify_code.html', {'error': 'Invalid code.'})

    return render(request, 'mypages/forgot_verify_code.html')


def reset_password_view(request):
    username = request.session.get('reset_user')
    if not username:
        return redirect('forgot_password')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('forgot_password')

    if request.method == 'POST':
        new_pass = request.POST['new_password']
        confirm = request.POST['confirm_password']

        if new_pass != confirm:
            return render(request, 'mypages/reset_password.html', {'error': 'Passwords do not match.'})

        try:

            validate_password(new_pass, user=user)
        except ValidationError as e:
            return render(request, 'mypages/reset_password.html', {
                'error': e.messages[0]
            })

        user.set_password(new_pass)
        user.save()
        login(request, user)

        request.session.pop('reset_user', None)
        request.session.pop('reset_code', None)

        return redirect('home')

    return render(request, 'mypages/reset_password.html')


def AccountView(request):
    try:
        Profile = request.user.profile
    except ProfileUser.DoesNotExist:
        Profile = ProfileUser(user=request.user)
    if request.method == 'GET':
        form = ProfileForm(instance=Profile)
    elif request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, "mypages/edit_account.html", {"form": form})
