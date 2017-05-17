# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import CustomQuoteForm, ContactForm


def get_index(request):
    return render(request, 'index.html')


def get_faq(request):
    return render(request, 'faq.html')


def get_instant_quote(request):
    return render(request, 'instant-quote.html')


def get_custom_quote(request):
    if request.method == 'POST':
        form = CustomQuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully submitted our Custom Quote Form")
            return redirect(reverse('customquoteconfirm'))
        else:
            form.add_error(None, "Your form does not seem to be valid")

    else:
        form = CustomQuoteForm()

    args = {'form': form}
    return render(request, 'custom-quote.html', args)


def get_custom_quote_confirm(request):
    return render(request, 'custom-quote-confirm.html')


def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully submitted our Contact Form")
            return redirect(reverse('contactconfirm'))
        else:
            form.add_error(None, "Your form does not seem to be valid")

    else:
        form = ContactForm()

    args = {'form': form}
    return render(request, 'contact.html', args)


def get_contact_confirm(request):
    return render(request, 'contact-confirm.html')