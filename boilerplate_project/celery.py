import os

import celery
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boilerplate_project.config.settings')
django.setup()

app = celery.Celery('config')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(force=True)
# app.autodiscover_tasks()
app.conf.timezone = 'UTC'
