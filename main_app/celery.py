import os
import django
from celery import Celery
from django.conf import settings
from celery.schedules import  crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')
django.setup()
app = Celery('main_app')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# from applications.spam.tasks import send_spam_message_to_users
# from datetime import timedelta
app.conf.beat_schedule ={
    'send-spam': {
        'task':'applications.spam.tasks.send_spam_message_to_users',
        'schedule': crontab(minute='*/1'),
    }
}