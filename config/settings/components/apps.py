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
    'cors_headers',
    'rest_framework',
    'admin_reorder',
]

# -----------------------------------------------------------------------------
# INSTALLED APPS SUM
# -----------------------------------------------------------------------------
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
