"""
WSGI config for examPRACTICE_python_ashwinchalaka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examPRACTICE_python_ashwinchalaka.settings")

application = get_wsgi_application()
