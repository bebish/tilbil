import os
import time
from celery.schedules import crontab
from celery import Celery
from config import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'reset-strike-status-every-night': {
        'task': 'account.tasks.reset_strike_status',
        'schedule': crontab(hour=0, minute=0),
    },
    'reset-strike-every-night': {
        'task': 'account.tasks.reset_strike',
        'schedule': crontab(hour=0, minute=0),
    },
    'reset-week_rating-every-week': {
        'task': 'account.tasks.reset_week_rating',
        'schedule': crontab(hour=0, minute=0, day_of_week=0),
    },
}