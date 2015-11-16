import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_connections.settings")
django.setup()

from app.models import *
p = Person()
p.first_name = 'f'
p.last_name = 'l'

