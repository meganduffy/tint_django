from django import forms
from .models import UploadFiles, TranscriptDetails
from .choices import *


class UploadFilesForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True})
    )

    class Meta:
        model = UploadFiles
        fields = ('file',)


class TranscriptDetailsForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES,
                                 widget=forms.Select(attrs={'onchange': 'calculateTotal()', 'id': 'category'}))
    text_format = forms.ChoiceField(choices=TEXT_FORMAT_CHOICES,
                                    widget=forms.Select(attrs={'onchange': 'calculateTotal()', 'id': 'style'}))
    num_speakers = forms.ChoiceField(choices=NUM_SPEAKER_CHOICES,
                                     widget=forms.Select(attrs={'onchange': 'calculateTotal()', 'id': 'speakers'}))
    timestamps = forms.ChoiceField(choices=TIMESTAMP_CHOICES,
                                   widget=forms.Select(attrs={'onchange': 'calculateTotal()', 'id': 'timestamps'}))
    tat = forms.ChoiceField(choices=TAT_CHOICES,
                            widget=forms.Select(attrs={'onchange': 'calculateTotal()', 'id': 'tat'}))
    audio_quality = forms.ChoiceField(choices=AUDIO_QUAL_CHOICES,
                                      widget=forms.Select(
                                          attrs={'onchange': 'calculateTotal()', 'id': 'audio-quality'}))

    class Meta:
        model = TranscriptDetails
        fields = ['category', 'text_format', 'num_speakers', 'timestamps',
                  'tat', 'audio_quality']
