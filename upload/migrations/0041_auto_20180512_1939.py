# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-12 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0040_auto_20170605_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcriptdetails',
            name='status',
            field=models.CharField(choices=[(b'Processing', b'Processing'), (b'InProgress', b'In Progress'), (b'Done', b'Done')], default='Processing', max_length=10),
        ),
        migrations.AlterField(
            model_name='uploadfiles',
            name='status',
            field=models.CharField(choices=[(b'Processing', b'Processing'), (b'InProgress', b'In Progress'), (b'Done', b'Done')], default='Processingpu', max_length=10),
        ),
    ]