# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0013_auto_20170520_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('InProcess', 'In Process'), ('Done', 'Done')], default='Todo', max_length=5),
        ),
    ]
