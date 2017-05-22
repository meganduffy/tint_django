from __future__ import unicode_literals
import uuid
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
        def find_total():
            multiplier = 0
            user_category_choice = request.POST.getlist('category', None)
            ucc = user_category_choice[0]
            print "CATEGORY CHOICE: %s" % ucc
            if ucc == "General" or ucc == "Personal":
                multiplier += 1.15
            elif ucc == "Legal" or ucc == "Medical":
                multiplier += 1.25
            else:
                multiplier += 0.99
            user_text_format_choice = request.POST.getlist('text_format', None)
            utfc = user_text_format_choice[0]
            print "TEXT_FORMAT: %s" % utfc
            if utfc == 'Verbatim':
                multiplier += 0.15
            user_num_speakers_choice = request.POST.getlist('num_speakers', None)
            unsc = user_num_speakers_choice[0]
            print "NUM_SPEAKERS: %s" % unsc
            if unsc == "3":
                multiplier += 0.05
            elif unsc == "4":
                multiplier += 0.1
            elif unsc == "10":
                multiplier += 0.15
            user_timestamps_choice = request.POST.getlist('timestamps', None)
            utsc = user_timestamps_choice[0]
            print "TIMESTAMPS: %s" % utsc
            if utsc == 'SpeakerChange' or utsc == '2Minutes':
                multiplier += 0.15
            user_tat_choice = request.POST.getlist('tat', None)
            utc = user_tat_choice[0]
            print "TAT: %s" % utc
            if utc == "24":
                multiplier += 0.35
            elif utc == "48":
                multiplier += 0.15
            user_audio_qual_choice = request.POST.getlist('audio_quality', None)
            uaqc = user_audio_qual_choice[0]
            print "AUDIO_QUAL: %s" % uaqc
            if uaqc == "Bad":
                multiplier += 0.1
            elif uaqc == "Fair":
                multiplier += 0.05
            total_time_num = total_time['file_length_mins__sum']
            return multiplier * total_time_num
        if form.is_valid():
            print
            transcript_details = form.save(commit=False)
            transcript_details.user = request.user
            transcript_details.total_price = find_total()
            transcript_details.save()
            messages.success(request, 'Form has been submitted!!')
            return redirect('orderreview')
    else:
        form = TranscriptDetailsForm()

    args = {'uploads': uploads, 'total_time': total_time, 'form': form}

    return render(request, "transcript-detail-form.html", args)


def get_order_review(request):
    uploads = UploadFiles.objects.filter(user=request.user, status='Processing')
    transcript_details = TranscriptDetails.objects.filter(user=request.user, status='Processing')
    total_time = UploadFiles.objects.filter(user=request.user, status='Processing').aggregate(Sum('file_length_mins'))

    args = {'uploads': uploads, 'transcript_details': transcript_details, 'total_time': total_time}

    return render(request, "order_review.html", args)