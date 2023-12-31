import time

from celery import Celery
from django.conf import settings

app = Celery('celery')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(10)
    print('hello from debug task')
