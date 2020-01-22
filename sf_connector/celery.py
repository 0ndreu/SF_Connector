import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sf_connector.settings')

app = Celery('sf_connector')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
N = 2   # Количество часов между запросами post
app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': {'connectorApp.tasks.post_vacancies',
                 'connectorApp.tasks.patch_vacancies'},
        'schedule': crontab(hour=N),
    },
}

