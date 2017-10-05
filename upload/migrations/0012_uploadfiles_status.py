# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0011_uploadfiles_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfiles',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Doing', 'Doing'), ('Done', 'Done')], default='Todo', max_length=5),
        ),
    ]
