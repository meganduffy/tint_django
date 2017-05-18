# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class UploadFiles(models.Model):
    audio_files = models.FileField(upload_to='client_files/audio_files')
    video_files = models.FileField(upload_to='client_files/audio_files')
