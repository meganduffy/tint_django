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
        label='Profile Image (Optional)'
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

    class Meta:
        model = User
        fields = ['email', 'location', 'company', 'phone_number', 'image']
        widgets = {'location': CountrySelectWidget()}

    email = forms.CharField(
        label='Update Email Address',
        widget=forms.EmailInput
    )

    location = CountryField(
        blank_label='Select Country'
    )

    company = forms.CharField(
        label='Add/Update Company Name'
    )

    phone_number = forms.CharField(
        label='Add/Update Phone Number'
    )

    image = forms.ImageField(
        label='Add/Update Profile Image'
    )
