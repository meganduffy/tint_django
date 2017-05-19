from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UploadFiles
from .forms import UploadFilesForm


def get_upload_file_form(request):
    if request.method == 'POST':
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            print "FORM IS VALID"
            for f in request.FILES.getlist('file'):
                # UploadFiles.objects.create(file=f)
                UploadFiles(file=f).save()
                print "file name:"
                print f
            messages.success(request, 'Your file(s) have been uploaded!')
            form.save()
            return redirect('index')
        else:
            print "FORM IS NOT VALID"
            messages.error(request, 'Form is not valid')

    else:
        form = UploadFilesForm()

    args = {'form': form}
    return render(request, 'upload-file-form.html', args)