# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


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

