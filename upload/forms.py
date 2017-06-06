from django import forms
from .models import UploadFiles, TranscriptDetails, Review
from .choices import *


class UploadFilesForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True})
    )

    class Meta:
        model = UploadFiles
        fields = ('file',)


class TranscriptDetailsForm(forms.ModelForm):

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES
    )
    text_format = forms.ChoiceField(
        choices=TEXT_FORMAT_CHOICES
    )
    num_speakers = forms.ChoiceField(
        choices=NUM_SPEAKER_CHOICES
    )
    timestamps = forms.ChoiceField(
        choices=TIMESTAMP_CHOICES
    )
    tat = forms.ChoiceField(
        choices=TAT_CHOICES
    )
    audio_quality = forms.ChoiceField(
        choices=AUDIO_QUAL_CHOICES
    )

    class Meta:
        model = TranscriptDetails
        fields = ['category', 'text_format', 'num_speakers', 'timestamps',
                  'tat', 'audio_quality']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
