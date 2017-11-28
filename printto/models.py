from django.db import models

# Create your models here.


class UploadedFileModel(models.Model):
    file = models.FileField(upload_to='upload/')
    datetime = models.DateTimeField(auto_now_add=True)
