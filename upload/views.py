# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, reverse
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import UploadFileForm


# class FileFieldView(FormView):
#     form_class = UploadFileForm
#     template_name = 'upload-file-form.html'
#     success_url = 'index'
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('audio_files')
#         if form.is_valid():
#             for f in files:
#                 f.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         form.save(commit=True)
#         messages.success(self.request, 'File uploaded!')
#         return super(FileFieldView, self).form_valid(form)
#
# for afile in request.FILES.getlist('files'):
#     File(file=afile, files=test).save()

def get_upload_file_form(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST)
        if form.is_valid():
            files = request.FILES.getlist('audio_files')
            for f in files:
                f.save()
            form.save()
            messages.success(request, 'File(s) have been uploaded')
        else:
            form.add_error(None, 'Something went wrong')
    else:
        form = UploadFileForm()

    args = {'form': form}
    return render(request, 'upload-file-form.html', args)