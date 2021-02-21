from split_settings.tools import optional, include
import os

DJANGO_ENV = os.environ.get('DJANGO_ENV', default='devel')

base_settings = (
    'components/common.py',
    'components/apps.py',
    'components/sentry.py',
    'components/logging.py',
    'components/services.py',
    'components/third_party_apps.py',
    optional('environments/%s.py' % DJANGO_ENV),
    )

include(*base_settings)
