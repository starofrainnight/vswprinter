import shutil
from django.apps import AppConfig
from . import APP_NAME


class PrinttoConfig(AppConfig):
    name = APP_NAME

    def ready(self):
        super().ready()

        from .models import UploadedFileModel

        # Clear printed items when start this app
        UploadedFileModel.objects.all().delete()
        shutil.rmtree("./upload", ignore_errors=True)
