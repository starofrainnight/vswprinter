from django.db import models
from .validators import validate_upload_file_extension


class UploadedFileModel(models.Model):
    file = models.FileField(upload_to='upload/',
                            validators=[validate_upload_file_extension])
    datetime = models.DateTimeField(auto_now_add=True)
