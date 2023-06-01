import time

from celery import shared_task
from JobSite.models import *


@shared_task
def sleep_def121():
    time.sleep(10)
    for i in range(20):
        print(Disease.objects.all())
    print("finish task")