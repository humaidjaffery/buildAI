from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'password1', 'password2') 

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if Account.objects.filter(email=email).exists():
                raise forms.ValidationError("Email is already in use.")
            return email