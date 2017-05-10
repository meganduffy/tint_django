# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def get_index(request):
    return render(request, 'index.html')


def get_faq(request):
    return render(request, 'faq.html')
