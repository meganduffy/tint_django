# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def get_index(request):
    return render(request, 'index.html')


def get_faq(request):
    return render(request, 'faq.html')


def get_instant_quote(request):
    return render(request, 'instant-quote.html')
