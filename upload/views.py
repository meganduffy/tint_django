from __future__ import unicode_literals
from math import ceil
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import UploadFiles, TranscriptDetails, Review
from .forms import UploadFilesForm, TranscriptDetailsForm, ReviewForm
from mutagen import File
import datetime


def get_audio_length(f):
    f = File(f).info.length
    return int(ceil(f / 60))


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

        def get_total_price():
            multiplier = 0

            category_choice = request.POST.getlist('category', None)[0]
            category_price = {'General': 1.15, 'Personal': 1.15, 'Legal': 1.25, 'Medical': 1.25, 'Academic': 0.99}.get(
                category_choice)
            multiplier += category_price

            text_format_choice = request.POST.getlist('text_format', None)[0]
            text_format_price = {'Verbatim': 0.15, 'IntelligentVerbatim': 0}.get(text_format_choice)
            multiplier += text_format_price

            num_speakers_choice = request.POST.getlist('num_speakers', None)[0]
            num_speakers_price = {'1': 0, '2': 0, '3': 0.5, '4': 0.1, '10': 0.15}.get(num_speakers_choice)
            multiplier += num_speakers_price

            timestamps_choice = request.POST.getlist('timestamps', None)[0]
            timestamps_price = {'None': 0, 'SpeakerChange': 0.15, '2Minutes': 0.15}.get(timestamps_choice)
            multiplier += timestamps_price

            tat_choice = request.POST.getlist('tat', None)[0]
            tat_price = {'24': 0.35, '48': 0.15, 'Standard': 0}.get(tat_choice)
            multiplier += tat_price

            audio_qual_choice = request.POST.getlist('audio_quality', None)[0]
            audio_qual_price = {'Good': 0, 'Fair': 0.05, 'Bad': 0.1}.get(audio_qual_choice)
            multiplier += audio_qual_price

            total_time_multiplier = total_time['file_length_mins__sum']
            return multiplier * total_time_multiplier

        if form.is_valid():
            print
            transcript_details = form.save(commit=False)
            transcript_details.user = request.user
            transcript_details.total_price = get_total_price()
            transcript_details.save()
            UploadFiles.objects.filter(user=request.user, status='Processing').update(
                transcript_details=transcript_details.id, status='In Progress')
            messages.success(request, 'Form has been submitted!!')
            return redirect('orderreview')
    else:
        form = TranscriptDetailsForm()

    args = {'uploads': uploads, 'total_time': total_time, 'form': form}

    return render(request, "transcript-detail-form.html", args)


@login_required(login_url='/login/')
def remove_file(request, upload_id):
    user_file = UploadFiles.objects.get(id=upload_id)
    user_file.delete()
    messages.success(request, '%s has been removed from your order!' % user_file.file_name)
    return redirect('/transcriptdetails')


@login_required(login_url='/login/')
def get_order_review(request):
    transcript_details = TranscriptDetails.objects.filter(user=request.user, status='Processing').order_by('-id')[:1]
    total_time = UploadFiles.objects.filter(user=request.user, status='Processing').aggregate(Sum('file_length_mins'))

    args = {'transcript_details': transcript_details, 'total_time': total_time}

    return render(request, "order_review.html", args)


@login_required(login_url='/login/')
def save_order_for_later(request, detail_id):
    TranscriptDetails.objects.filter(id=detail_id).update(saved=True)
    messages.success(request, 'Order Number %s has been moved to Saved For Later' % detail_id)
    return redirect('/saved-for-later')


@login_required(login_url='/login/')
def get_saved_for_later(request):
    transcript_details = TranscriptDetails.objects.filter(user=request.user, status='Processing', saved=True).order_by(
        '-id')
    total_time = UploadFiles.objects.filter(user=request.user, status='Processing').aggregate(Sum('file_length_mins'))

    args = {'transcript_details': transcript_details, 'total_time': total_time}

    return render(request, "saved-for-later.html", args)


@login_required(login_url='/login/')
def get_transcript_tracker(request):
    transcript_details = TranscriptDetails.objects.filter(user=request.user, status='InProgress').order_by(
        '-purchased_at')

    args = {'transcript_details': transcript_details}
    return render(request, "transcript-tracker.html", args)


def new_review(request, detail_id):
    transcript_detail = get_object_or_404(TranscriptDetails, pk=detail_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(False)
            review.transcript_detail = transcript_detail
            review.user = request.user
            review.save()

            messages.success(request, "Thank you for your review!")
            return redirect(reverse('transcript_tracker'))
    else:
        form = ReviewForm()

    args = {
        'form': form,
        'form_action': reverse('new_review', args={detail_id}),
        'button_text': 'Leave a Review'
    }
    args.update(csrf(request))
    return render(request, 'review_form.html', args)


def edit_review(request, detail_id, review_id):
    transcript_detail = get_object_or_404(TranscriptDetails, pk=detail_id)
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully edited your review!")
            return redirect(reverse('transcript_tracker'))
    else:
        form = ReviewForm(instance=review)

    args = {
        'form': form,
        'form_action': reverse('edit_review', kwargs={"detail_id": transcript_detail.id, "review_id": review.id}),
        'button_text': 'Edit Review'
    }
    args.update(csrf(request))
    return render(request, 'review_form.html', args)
