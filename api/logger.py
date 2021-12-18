import datetime as dt
import logging
import os
import sys

from pythonjsonlogger import jsonlogger

APP_ENV_DEV = 'DEV'
APP_ENV_PROD = 'PROD'
APP_ENV = os.getenv('APP_ENV', APP_ENV_DEV)


def get_logger(name='logg', level=logging.INFO):
    """Returns a logger with the given name and level"""

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if APP_ENV == APP_ENV_PROD:
        # Create a gurnicorn logging handler
        handler, _  = get_gunicorn_handler()
        if handler is None:
            # App is not invoked by Gunicorn, get a stream logger
            handler = get_stream_handler(level)

        # Attach handlers to python root logger
        logger.addHandler(handler)
    else:
        # Get a stream handler
        handler =  get_stream_handler(level)

        logger.addHandler(handler)

    return logger


def get_gunicorn_handler():
    """Returns a logger which will add flask logs within gunicorn logs and
    also adhere to the logging level set by gunicorn"""

    # Set up logging via gunicorn
    gunicorn_logger = logging.getLogger('gunicorn.error')

    # Set gunicorn as log handler
    if gunicorn_logger.handlers:
        hdlr = gunicorn_logger.handlers[0]
        # Add json formatter
        formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
        hdlr.setFormatter(formatter)
    else:
        hdlr = None

    # Let gunicorn set the logging level
    lvl = gunicorn_logger.level

    return hdlr, lvl


def get_stream_handler(level):
    """Returns a stream logging handler"""

    # Create a stream stdout handler
    hdlr = logging.StreamHandler(sys.stdout)
    hdlr.setLevel(level)
    # Add json formatter
    formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
    hdlr.setFormatter(formatter)

    return hdlr


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """
    A customized json formatter that adds timestamp, name and log level data
    """
    def add_fields(self, log_record, record, message_dict):
        """
        Hijacks the internal add_fields method and add extra meta data to a log
        records
        """
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)

        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = dt.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

