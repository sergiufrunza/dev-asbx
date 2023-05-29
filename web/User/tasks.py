import time

from celery import shared_task


@shared_task
def sleep_def121():
    time.sleep(10)
    for i in range(20):
        print(i)
    print("finish task")