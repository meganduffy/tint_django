# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0016_auto_20170520_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcriptdetails',
            name='audio_quality',
            field=models.CharField(choices=[('Bad', 'Bad'), ('Fair', 'Fair'), ('Good', 'Good')], default='Fair', max_length=4),
        ),
        migrations.AddField(
            model_name='transcriptdetails',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Legal', 'Legal'), ('Medical', 'Medical'), ('Personal', 'Personal'), ('Academic', 'Academic')], default='General', max_length=8),
        ),
        migrations.AddField(
            model_name='transcriptdetails',
            name='num_speakers',
            field=models.CharField(choices=[(1, '1 Speaker'), (2, '2 Speakers'), (3, '3 Speakers'), (4, '4+ Speakers'), (10, '10+ Speakers')], default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='transcriptdetails',
            name='tat',
            field=models.CharField(choices=[(24, '24 Hour'), (48, '48 Hour'), ('Standard', 'Standard (Up To 4 Days)')], default='Standard', max_length=8),
        ),
        migrations.AddField(
            model_name='transcriptdetails',
            name='text_format',
            field=models.CharField(choices=[('IntelligentVerbatim', 'Intelligent Verbatim'), ('Verbatim', 'Full Verbatim')], default='IntelligentVerbatim', max_length=19),
        ),
        migrations.AddField(
            model_name='transcriptdetails',
            name='timestamps',
            field=models.CharField(choices=[('None', 'Not Required'), ('SpeakerChange', 'On Speaker Change'), ('2Minutes', 'Every Two Minutes')], default='None', max_length=13),
        ),
    ]
