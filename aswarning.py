import contextlib
import os
import traceback
import warnings


@contextlib.contextmanager
def as_warning(message=None, warning_class=None):
    if message is None:
        message = ''
    if warning_class is None:
        warning_class = Warning
    try:
        yield
    except:
        warnings.warn(message + os.linesep + traceback.format_exc(), warning_class)
