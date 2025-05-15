"""
ASGI config for healthcare project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')

application = get_asgi_application()   

#ASGI application. This object is used by ASGI servers to forward HTTP, WebSocket, or other protocols to your Django app.
