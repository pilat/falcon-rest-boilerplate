import logging
import time

from core.conf import settings


class JavaLogFormatter(logging.Formatter):
    converter = time.gmtime

    def format(self, record):
        if record.threadName == 'MainThread':
            record.threadName = 'MainTh-0'
        record.funcName = record.funcName.replace('<', '').replace('>', '')

        ret = super().format(record)

        no_extra = ('name', 'msg', 'args', 'levelname', 'levelno', 'pathname',
                    'filename', 'module', 'exc_info', 'exc_text', 'stack_info',
                    'lineno', 'funcName', 'created', 'msecs', 'processName',
                    'relativeCreated', 'thread', 'threadName', 'process',
                    'asctime', 'message')
        extra_keys = [(k, v) for k, v in record.__dict__.items()
                      if k not in no_extra]

        for k, v in extra_keys:
            ret = '%s, %s=%s' % (ret, k, v)
        return ret


def on_ready(app):
    app_formatter = JavaLogFormatter(
        '%(asctime)s,%(msecs)03d [%(threadName)s]  %(levelname)s  '
        '%(name)s.%(funcName)s  -  %(message)s; pid: %(process)d',
        datefmt='%Y-%m-%d %H:%M:%S')

    app_handler = logging.StreamHandler()
    app_handler.setLevel(logging._nameToLevel[settings.base_loglevel])
    app_handler.setFormatter(app_formatter)
    logging.getLogger('').addHandler(app_handler)

    # change log levels:
    for name, level in settings.logging.items():
        if level not in logging._nameToLevel:
            raise ValueError("Unknown error level: %r" % level)
        level_id = logging._nameToLevel[level]
        logging.getLogger(name).setLevel(level_id)
