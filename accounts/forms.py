from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    image = forms.ImageField(
        label='Profile Image (Optional)',
        required=False
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'image']
        exclude = ['username', 'location', 'company', 'phone_number']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    email = forms.CharField(
        label='Email Address'
    )
    if not email:
        message = 'Please enter your email address'
        raise forms.ValidationError(message)

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        # automatically set to email address to create a unique identifier
        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        required=False
    )

    last_name = forms.CharField(
        required=False
    )

    company = forms.CharField(
        required=False
    )

    phone_number = forms.CharField(
        required=False
    )

    image = forms.ImageField(
        required=False
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'location', 'company', 'phone_number', 'image']
        widgets = {'location': CountrySelectWidget()}
