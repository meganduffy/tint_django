from __future__ import unicode_literals
from math import ceil
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import UploadFiles, TranscriptDetails
from .forms import UploadFilesForm, TranscriptDetailsForm
from mutagen import File


def get_audio_length(f):
    f = File(f).info.length
    return int(ceil(f/60))


@login_required(login_url='/login/')
def get_upload_file_form(request):
    if request.method == 'POST':
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            print request.FILES.getlist('file')
            for f in request.FILES.getlist('file'):
                print f
                time = get_audio_length(f)
                UploadFiles(file=f, file_name=f, file_length_mins=time, user=request.user).save()
            messages.success(request, 'Your file(s) have been uploaded!')

            return redirect('transcriptdetails')
        else:
            print "FORM IS NOT VALID"
            print(form.errors)
            messages.error(request, 'Form is not valid')

    else:
        form = UploadFilesForm()

    args = {'form': form}
    return render(request, 'upload-file-form.html', args)


@login_required(login_url='/login/')
def get_transcript_detail_form(request):
    uploads = UploadFiles.objects.filter(user=request.user, status='Processing')
    total_time = UploadFiles.objects.filter(user=request.user, status='Processing').aggregate(Sum('file_length_mins'))
    if request.method == 'POST':
        form = TranscriptDetailsForm(request.POST)
        if form.is_valid():
            transcript_details = form.save(commit=False)
            transcript_details.user = request.user
            transcript_details.save()
            messages.success(request, 'Form has been submitted!!')
            return redirect('index')
    else:
        form = TranscriptDetailsForm()

    args = {'uploads': uploads, 'total_time': total_time, 'form': form}

    return render(request, "transcript-detail-form.html", args)
