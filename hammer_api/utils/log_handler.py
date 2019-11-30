import time
import os
import logging
from logging.handlers import BaseRotatingHandler
from gunicorn.glogging import Logger as GLogger
from gunicorn import util

try:
    import codecs
except ImportError:
    codecs = None


class MultiProcessSafeDailyRotatingFileHandler(BaseRotatingHandler):
    """Similar with `logging.TimedRotatingFileHandler`, while this one is
    - Multi process safe
    - Rotate at midnight only
    - Utc not supported
    """
    def __init__(self, filename, encoding=None, delay=False, utc=False, **kwargs):
        self.utc = utc
        self.suffix = "%Y-%m-%d"
        self.baseFilename = filename
        self.currentFileName = self._compute_fn()
        BaseRotatingHandler.__init__(self, filename, 'a', encoding, delay)

    def shouldRollover(self, record):
        if self.currentFileName != self._compute_fn():
            return True
        return False

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        self.currentFileName = self._compute_fn()

    def _compute_fn(self):
        return self.baseFilename + "." + time.strftime(self.suffix, time.localtime())

    def _open(self):
        if self.encoding is None:
            stream = open(self.currentFileName, self.mode)
        else:
            stream = codecs.open(self.currentFileName, self.mode, self.encoding)
        # simulate file name structure of `logging.TimedRotatingFileHandler`
        if os.path.exists(self.baseFilename):
            try:
                os.remove(self.baseFilename)
            except OSError:
                pass
        try:
            os.symlink(self.currentFileName, self.baseFilename)
        except OSError:
            pass
        return stream


class RotatingGLogger(GLogger):
    """将 Gunicorn 的默认 Logger 使用的 Handler 从 FileHandler 改为其他"""
    def _set_handler(self, log, output, fmt, stream=None):
        # remove previous gunicorn log handler
        h = self._get_gunicorn_handler(log)
        if h:
            log.handlers.remove(h)

        if output is not None:
            if output == "-":
                h = logging.StreamHandler(stream)
            else:
                util.check_is_writeable(output)
                h = MultiProcessSafeDailyRotatingFileHandler(output)
                # make sure the user can reopen the file
                try:
                    os.chown(h.baseFilename, self.cfg.user, self.cfg.group)
                except OSError:
                    # it's probably OK there, we assume the user has given
                    # /dev/null as a parameter.
                    pass

            h.setFormatter(fmt)
            h._gunicorn = True
            log.addHandler(h)


class SingleLevel(logging.Filter):
    def __init__(self, level):
        if isinstance(level, int):
            self.allow = level
        elif isinstance(level, str):
            self.allow = getattr(logging, level)
        else:
            raise ValueError('Invalid `level` type.')

    def filter(self, record):
        if record.levelno == self.allow:
            return True
        else:
            return False
