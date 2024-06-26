from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, TaxiDriver, Client

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_driver', 'is_client')

class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = TaxiDriver
        fields = ('license_number', 'taxi_number', 'phone')

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('address', 'phone')