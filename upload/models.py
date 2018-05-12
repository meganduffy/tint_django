# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from tinymce.models import HTMLField
from .choices import *
from .validators import validate_file_extension


class UploadFiles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='uploads')
    transcript_details = models.ForeignKey('TranscriptDetails', related_name='uploaded_files', blank=True, null=True)
    file = models.FileField(upload_to='client_files/%Y/%m/%d', validators=[validate_file_extension], blank=True,
                            null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    file_name = models.CharField(max_length=500, default='')
    file_length_mins = models.CharField(max_length=255, default='', blank=True, null=True)
    status = models.CharField(max_length=100, default='Processing', choices=STATUS_CHOICES)


class TranscriptDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transcript_details')
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES)
    text_format = models.CharField(max_length=19, choices=TEXT_FORMAT_CHOICES)
    num_speakers = models.CharField(max_length=2, choices=NUM_SPEAKER_CHOICES)
    timestamps = models.CharField(max_length=13, choices=TIMESTAMP_CHOICES)
    tat = models.CharField(max_length=8, choices=TAT_CHOICES)
    audio_quality = models.CharField(max_length=4, choices=AUDIO_QUAL_CHOICES)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=100, default='Processing', choices=STATUS_CHOICES)
    saved = models.BooleanField(default=False)
    purchased_at = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.total_price,
            "currency": "EUR",
            "item_name": "%s-%s Transcript" % (self.category, self.text_format),
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL,
            "custom": "%s-%s" % (self.pk, self.tat)
        }
        return PayPalPaymentsForm(initial=paypal_dict)

    @property
    def is_past_due(self):
        return timezone.now() > self.deadline


class Review(models.Model):
    transcript_detail = models.ForeignKey(TranscriptDetails, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
    comment = HTMLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)


from .signals import payment_accepted, invalid_handler

valid_ipn_received.connect(payment_accepted)

invalid_ipn_received.connect(invalid_handler)
