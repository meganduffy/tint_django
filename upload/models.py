# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from .choices import *


class UploadFiles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='uploads')
    file = models.FileField(upload_to='client_files/%Y/%m/%d', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    file_name = models.CharField(max_length=500, default='')
    file_length_mins = models.CharField(max_length=255, default='', blank=True, null=True)
    status = models.CharField(max_length=5, default='Processing', choices=STATUS_CHOICES)


class TranscriptDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transcript_details')
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES)
    text_format = models.CharField(max_length=19, choices=TEXT_FORMAT_CHOICES)
    num_speakers = models.CharField(max_length=2, choices=NUM_SPEAKER_CHOICES)
    timestamps = models.CharField(max_length=13, choices=TIMESTAMP_CHOICES)
    tat = models.CharField(max_length=8, choices=TAT_CHOICES)
    audio_quality = models.CharField(max_length=4, choices=AUDIO_QUAL_CHOICES)

