from django import forms
from .models import UploadedFileModel


class UploadedFileForm(forms.ModelForm):

    class Meta:
        model = UploadedFileModel
        fields = ('file', )
