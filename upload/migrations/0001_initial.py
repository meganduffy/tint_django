# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-12 20:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models
import upload.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', tinymce.models.HTMLField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TranscriptDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[(b'General', b'General'), (b'Legal', b'Legal'), (b'Medical', b'Medical'), (b'Personal', b'Personal'), (b'Academic', b'Academic')], max_length=8)),
                ('text_format', models.CharField(choices=[(b'IntelligentVerbatim', b'Intelligent Verbatim'), (b'Verbatim', b'Full Verbatim')], max_length=19)),
                ('num_speakers', models.CharField(choices=[(b'1', b'1 Speaker'), (b'2', b'2 Speakers'), (b'3', b'3 Speakers'), (b'4', b'4+ Speakers'), (b'10', b'10+ Speakers')], max_length=2)),
                ('timestamps', models.CharField(choices=[(b'None', b'Not Required'), (b'SpeakerChange', b'On Speaker Change'), (b'2Minutes', b'Every Two Minutes')], max_length=13)),
                ('tat', models.CharField(choices=[(b'24', b'24 Hour'), (b'48', b'48 Hour'), (b'Standard', b'Standard (Up To 4 Days)')], max_length=8)),
                ('audio_quality', models.CharField(choices=[(b'Bad', b'Bad'), (b'Fair', b'Fair'), (b'Good', b'Good')], max_length=4)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[(b'Processing', b'Processing'), (b'InProgress', b'In Progress'), (b'Done', b'Done')], default='Processing', max_length=100)),
                ('saved', models.BooleanField(default=False)),
                ('purchased_at', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transcript_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='client_files/%Y/%m/%d', validators=[upload.validators.validate_file_extension])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('file_name', models.CharField(default='', max_length=500)),
                ('file_length_mins', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('status', models.CharField(choices=[(b'Processing', b'Processing'), (b'InProgress', b'In Progress'), (b'Done', b'Done')], default='Processing', max_length=100)),
                ('transcript_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to='upload.TranscriptDetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='transcript_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='upload.TranscriptDetails'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
