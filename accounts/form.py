from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True,
                             help_text='Required. Enter a valid email address.')
    address_line1 = forms.CharField(
        max_length=255, required=True, help_text='Required.')
    city = forms.CharField(max_length=255, required=True,
                           help_text='Required.')
    state = forms.CharField(
        max_length=255, required=True, help_text='Required.')
    pincode = forms.CharField(
        max_length=6, required=True, help_text='Required.')
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2', 'address_line1', 'city', 'state', 'pincode', 'profile_picture',)
