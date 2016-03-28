# -*- coding: utf-8 -*-
"""
Example configuration for GEAStarterKit
"""


##
## Authentication/authorizationc config
import authomatic

from authomatic.providers import oauth2
from collections import OrderedDict

AUTHOMATIC_CONFIG = OrderedDict([
    ('github', {
        'name': 'Github',

        'class_': oauth2.GitHub,
        'consumer_key': 'ADD YOURS',
        'consumer_secret': 'AD YOURS',

        'id': authomatic.provider_id(),

        'icon': 'github',

        'scope': ['user:email']
    }),

    ('google', {
        'name': 'Google',

        'id': authomatic.provider_id(),

        'icon': 'google'
    }),
])

SECRET_STRING = 'YOUR SECRET KEY'
DEVELOPMENT = True

#
# Origin address for system emails.
email_from_address = 'root@localhost'

#
# Options for login manager
max_days_verification = 30
max_hours_password_reset = 48

#
# How long to time.sleep() when an invalid login, token, or similar is tried.
security_wait = 3

#
# Langauges application supports
languages = {
    'en': 'English'
}

#
# Whether to use Paste debug panel while in development
enable_debug_panel = True

#
# What to import automatically
install_apps = [
    'apps.error_pages',
    'apps.users',
    'apps.simplecms',
    'apps.email',
    'apps.admin'
]
