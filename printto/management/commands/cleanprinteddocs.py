# -*- coding: utf-8 -*-

import os
import arrow
from django.core.management.base import BaseCommand
from printto.models import UploadedFileModel


class Command(BaseCommand):
    help = 'Clean all printed docs after 3 minutes'

    def handle(self, *args, **options):
        now_time = arrow.now()
        now_time = now_time.shift(minutes=-3)
        now_time = now_time.datetime

        records = UploadedFileModel.objects.filter(datetime__lt=now_time)
        for record in records:
            try:
                os.remove(record.file.path)
            except:
                pass

        if records:
            records.delete()
