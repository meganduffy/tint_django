from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

REFERRAL_CHOICES = (
    ('WEB', 'Web Search'),
    ('FB', 'Facebook'),
    ('DD', 'DoneDeal'),
    ('GT', 'GumTree'),
    ('WOM', 'Word of Mouth'),
    ('O', 'Other')
)


class CustomQuote(models.Model):
    """
    Model for Custom Quote Form
    """
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    email1 = models.CharField(max_length=255, default='')
    email2 = models.CharField(max_length=255, default='')
    location = CountryField(blank=True, null=True)
    company = models.CharField(max_length=255, default='', blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    existing_client = models.BooleanField()
    new_client = models.BooleanField()
    referral = models.CharField(max_length=3, choices=REFERRAL_CHOICES, blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)
    audio_minutes = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.email1


class Contact(models.Model):
    """
    Model for Contact Form
    """
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=255, default='')
    location = CountryField(blank=True, null=True)
    company = models.CharField(max_length=255, default='', blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    message = models.TextField(default='')

    def __unicode__(self):
        return self.email
