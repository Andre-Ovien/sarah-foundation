"""
WSGI config for SarahFoundation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
from django.contrib.auth import get_user_model

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SarahFoundation.settings')

application = get_wsgi_application()



User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="andy",
        email="andy@gmail.com",
        password="andy12345"
    )
    print("Superuser 'admin' created automatically!")
