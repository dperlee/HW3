"""
WSGI config for HW3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HW3.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# dj-static configuration
# See: https://github.com/kennethreitz/dj-static
application = Cling(get_wsgi_application())
