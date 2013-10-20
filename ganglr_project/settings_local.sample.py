import os.path
from settings import PWD

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# From Facebook app registration
SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2',
                                                 # 'mysql', 'sqlite3' or
                                                 # 'oracle'.
        'NAME': 'ganglr.db',                     # Or path to database file if
                                                 # using sqlite3.

        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or
                     # '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PWD, '../upload')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# For Django debug toolbar
INTERNAL_IPS = ('127.0.0.1',)