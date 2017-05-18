# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.core.validators import RegexValidator


class AccountUserManager(UserManager):

    def _create_user(self, username, email, password,
                    is_staff, is_superuser, image, **extra_fields):
        """
        Creates user with email set to username
        """
        now = timezone.now()
        if not email:
            raise ValueError('The username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          date_joined=now, image=image, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    objects = AccountUserManager()
    last_login = models.DateTimeField(default=timezone.now)
    previous_login = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    first_name = models.CharField(max_length=255, default='', blank=True, null=True)
    last_name = models.CharField(max_length=255, default='', blank=True, null=True)
    location = CountryField(blank=True, null=True)
    company = models.CharField(max_length=255, default='', blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)


