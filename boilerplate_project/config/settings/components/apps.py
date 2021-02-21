# -----------------------------------------------------------------------------
# Apps configs
# ALL PACKAGES FOR DJANGO APP
# -----------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# -----------------------------------------------------------------------------
# LOCAL APPS
# -----------------------------------------------------------------------------
LOCAL_APPS = []

# -----------------------------------------------------------------------------
# THIRD PARTY APPS
# -----------------------------------------------------------------------------
THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'django_celery_results',
    'django_celery_beat',
    'rest_framework.authtoken',
    # 'django_json_widget',
    'easy_select2',
    'admin_reorder',
]

# -----------------------------------------------------------------------------
# INSTALLED APPS SUM
# -----------------------------------------------------------------------------
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
