from django import forms
from .models import UploadFiles


class UploadFilesForm(forms.ModelForm):

    class Meta:
        model = UploadFiles
        fields = ('file',)
