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
    ('google', {
        'name': 'Google',

        'id': authomatic.provider_id(),

        'icon': 'google'
    }),
])

SECRET_STRING = 'TESTING KEY'
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
security_wait = .1

#
# Langauges application supports
languages = {
    'en': 'English'
}

#
# Whether to use Paste debug panel while in development
enable_debug_panel = False

#
# Where to send user when he logs in if nothing else is set.
default_view = 'users.profile'

#
# Name of the site/product
site_name = 'GAEStarterKit'

#
# What to import automatically
install_apps = [
    'apps.welcomekit',
    'apps.simplecms',
    'apps.error_pages',
    'apps.users',
    'apps.tenants',
    'apps.email',
    'apps.admin',
]
