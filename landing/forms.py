from django import forms
from .models import CustomQuote, Contact
from django.core.exceptions import ValidationError
from django_countries.widgets import CountrySelectWidget


class CustomQuoteForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name *')

    last_name = forms.CharField(label='Second Name *')

    email1 = forms.CharField(
        label='Email Address *',
        widget=forms.EmailInput
    )

    email2 = forms.CharField(
        label='Confirm Email Address *',
        widget=forms.EmailInput
    )

    existing_client = forms.BooleanField(required=False)

    new_client = forms.BooleanField(required=False)

    description = forms.CharField(label='Description of Project',
                                  widget=forms.Textarea)

    audio_minutes = forms.IntegerField(label='Estimated Time of Audio In Minutes *')

    class Meta:
        model = CustomQuote
        fields = ['first_name', 'last_name', 'email1', 'email2',
                  'location', 'company', 'phone_number', 'existing_client',
                  'new_client', 'referral']
        widgets = {'location': CountrySelectWidget()
                   # 'first_name': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
                   # 'last_name': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
                   # 'email1': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
                   # 'email2': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
                   # 'location': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
                   # 'company': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
                   # 'phone_number': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
                   # 'existing_client': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
                   # 'referral': forms.TextInput(attrs={'class': 'form-control col-sm-6'})
                   }

    def clean_email2(self):
        email1 = self.cleaned_data.get('email1')
        email2 = self.cleaned_data.get('email2')

        if email1 and email2 and email1 != email2:
            message = "Emails do not match"
            raise ValidationError(message)

        return email2


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name *')

    last_name = forms.CharField(label='Second Name *')

    email = forms.CharField(
        label='Email Address *',
        widget=forms.EmailInput
    )

    message = forms.CharField(label='Message *',
                              widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'location',
                  'company', 'phone_number', 'message']
