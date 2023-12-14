import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skarby.settings')

celery = Celery('skarby')

celery.config_from_object('django.conf:settings', namespace='CELERY')

celery.autodiscover_tasks()


# celery.conf.beat_schedule = {
#     'every': {
#         'task': 'users.tasks.count_new_users_weekly',
#         'schedule': 5.0
#     },
# }

celery.conf.beat_schedule = {
    'count-new-users-weekly': {
        'task': 'users.tasks.count_new_users_weekly',
        'schedule': crontab(day_of_week='monday', hour=15, minute=00),
    },
}

