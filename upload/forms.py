from django import forms
from .models import UploadFiles


class UploadFileForm(forms.Form):
    audio_files = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True})
    )
    video_files = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True})
    )


    class Meta:
        model = UploadFiles
        fields = ['audio_files', 'video_files']

# def clean(self):
#     cleaned_data = self.cleaned_data
#     file = cleaned_data.get("audio_file")
#     file_exts = ('.mp3', )
#
#     if file is None:
#
#         raise forms.ValidationError('Please select file first ')
#
#     if not file.content_type in settings.UPLOAD_AUDIO_TYPE:  # UPLOAD_AUDIO_TYPE contains mime types of required file
#
#         raise forms.ValidationError( 'Audio accepted only in: %s' % ' '.join( file_exts ) )
#
#
#     return cleaned_data
