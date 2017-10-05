# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 19:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20170517_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=b'', max_length=40)),
                ('last_name', models.CharField(default=b'', max_length=40)),
                ('email', models.CharField(default=b'', max_length=255)),
                ('location', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('company', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')])),
                ('message', models.TextField(default=b'')),
            ],
        ),
        migrations.AlterField(
            model_name='customquote',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')]),
        ),
    ]