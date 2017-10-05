# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import upload.validators


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0033_uploadfiles_transcript_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='client_files/%Y/%m/%d', validators=[upload.validators.validate_file_extension]),
        ),
    ]