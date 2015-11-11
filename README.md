# django_connections
sample for handling OperationalError in django.db

Scenario
-------
```
from ipython
%run ipython.py
from app.models import *
p = Person()
p.first_name = 'f'
p.last_name = 'l'
!sudo service mysql restart
p.save()
```
