# -*- coding: utf-8 -*-

import sys
import os
import os.path
import functools
from django.core.management import call_command
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(
    functools.partial(call_command, "cleanprinteddocs"), 'interval', minutes=1)
