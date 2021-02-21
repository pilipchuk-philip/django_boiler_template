import os

# -----------------------------------------------------------------------------
# THIRD PARTY APPS SETTINGS
# -----------------------------------------------------------------------------

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL',
                           default='redis://redis_container:6379')
TIME_ZONE = 'UTC'

# -----------------------------------------------------------------------------
# CELERY
# -----------------------------------------------------------------------------
CELERY_TIMEZONE = "Europe/Berlin"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', default=CELERY_BROKER_URL)
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND',
                                       default=CELERY_BROKER_URL)
# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60

# CELERY_RESULT_EXPIRES = 7 * 86400  # 7 days
# CELERY_SEND_EVENTS = True
#
# # CELERY_BROKER_USE_SSL = True
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE
# CELERY_ENABLE_UTC = True
# CELERY_TASK_DEFAULT_QUEUE = 'normal'
# CELERY_TASK_DEFAULT_EXCHANGE = 'default'
# CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'direct'
# CELERY_TASK_DEFAULT_ROUTING_KEY = 'normal'
# # CELERY_APP = 'boilerplate_project'
#
# CELERY_IMPORTS = (
#     'boilerplate_project',
# )

# -----------------------------------------------------------------------------
# REST_FRAMEWORK
# -----------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication', ],
}

# REST_FRAMEWORK = {
# 'DEFAULT_PERMISSION_CLASSES': [
# 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
# ]
# }

# -----------------------------------------------------------------------------
# CONS_SETTINGS
# -----------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True

# -----------------------------------------------------------------------------
# Admin reorder
# -----------------------------------------------------------------------------

ADMIN_REORDER = (
    # Keep original label and models
    # {'app': 'my_app', 'models': (
        # 'my_app.JobPosting',
        # 'my_app.FeedPartner',
        # 'my_app.Application',
    # )},
    'authtoken',
    'django_celery_beat',
    {'app': 'auth', 'models': ('auth.User', 'auth.Group')},
)
