import os
from .base import *

DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1')

# Allow hosts from environment or defaults
allowed_env = os.environ.get('ALLOWED_HOSTS', '*')
ALLOWED_HOSTS = [h.strip() for h in allowed_env.split(',') if h.strip()]

# Reverse Proxy SSL Header for Nginx Proxy Manager
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# CSRF Trusted Origins
csrf_env = os.environ.get('CSRF_TRUSTED_ORIGINS', 'https://pissyvibes.regies.tech,http://pissyvibes.regies.tech,https://*.regies.tech,http://*.regies.tech')
CSRF_TRUSTED_ORIGINS = [o.strip() for o in csrf_env.split(',') if o.strip()]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = False

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

db_url = os.environ.get('DATABASE_URL')
if db_url and db_url.startswith('postgres'):
    import urllib.parse as urlparse
    url = urlparse.urlparse(db_url)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port or 5432,
        }
    }

