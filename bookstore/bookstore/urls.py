"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from account.views import signupView, home, loginView, verify_email, forgot_password_view, verify_forgot_code_view, reset_password_view, AccountView
from django.contrib.auth.views import LogoutView, LoginView
import books

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", signupView, name="signup"),
    path("home/", home, name="home"),  # صفحه‌ی اصلی
    path("logout/", LogoutView.as_view(next_page='/login/'), name="logout"),
    path("", loginView, name="loginPage"),
    path('books/', include('books.urls')),  # تغییر مسیر از home به books
    path('Account/', AccountView, name="MyAccount"),
    path('signup/verify/', verify_email, name="verify_email"),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('forgot-password/verify/', verify_forgot_code_view, name='verify_forgot_code'),
    path('forgot-password/reset/', reset_password_view, name='reset_password'),
]


