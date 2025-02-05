"""
ASGI config for farm_tools project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

setting_module= 'farm_tools.deployment' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'farm_tools.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_tools.settings')

application = get_asgi_application()
