# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth import login as register_login
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from upload.models import TranscriptDetails


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
            register_login(request, user)
            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, 'Unable to log you in at this time!')

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register-form.html', args)


@login_required(login_url='/login/')
def profile(request):
    saved = TranscriptDetails.objects.filter(user=request.user, saved=True)
    args = {'saved': saved}
    return render(request, 'profile.html', args)


@login_required(login_url='/login/')
def edit_profile(request):

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            print "FORM IS VALID"
            user = request.user
            if request.POST.get('first_name', False):
                user.first_name = request.POST.get('first_name', False)
            if request.POST.get('last_name', False):
                user.last_name = request.POST.get('last_name', False)
            if request.POST.get('company', False):
                user.company = request.POST.get('company', False)
            if request.POST.get('phone_number', False):
                user.phone_number = request.POST.get('phone_number', False)
            if request.POST.get('location', False):
                user.location = request.POST.get('location', False)
            user.save()

            form.save()

            return redirect(profile)
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit-profile.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                user.previous_login = user.last_login
                user.save()
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))

