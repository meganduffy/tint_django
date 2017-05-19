# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class UploadFiles(models.Model):
    file = models.FileField(upload_to='client_files/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
