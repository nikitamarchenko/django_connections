import logging
import time


from django.db import models
from django.db import connection
from django.db import OperationalError


def is_connection_usable():
    try:
        connection.connection.ping()
    except OperationalError:
        return False
    else:
        return True


class ReconnectMixin(object):

    def save(self, *args, **kwargs):

        tries = 30
        while tries:

            try:
                return super(ReconnectMixin, self).save(*args, **kwargs)
            except OperationalError as exc:
                logging.warning('', exc_info=1)

                connection.close()

                tries -= 1
                sleep = 2 if tries > 20 else 60
                time.sleep(sleep)

        logging.exception('')

        raise exc


class Person(ReconnectMixin, models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
