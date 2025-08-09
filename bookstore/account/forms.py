# account/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import ProfileUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(forms.ModelForm):
    gender_choices = [("male", "male"), ("female", "female")]
    gender = forms.ChoiceField(choices=gender_choices, required=False)

    class Meta:
        model = ProfileUser
        fields = ['firstName', 'lastName', 'birthday', 'gender', 'phone']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

        def clean_phone(self):
            phone = self.cleaned_data.get('phone')
            if phone:
                if not phone.startswith('09'):
                    self.add_error('phone', "telphone should start with 09")
                if len(phone) != 11:
                    self.add_error('phone', "telphoe should be 11 digits")
            return phone

        def clean(self):
            cleaned_data = super().clean()
            fname = cleaned_data.get('firstName')
            lname = cleaned_data.get('lastName')
            if fname == lname:
                self.add_error(
                    'firstName', "first Name cant be same as last name")
                self.add_error(
                    'lastName', "first Name cant be same as last name")
            return cleaned_data
