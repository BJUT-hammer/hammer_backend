# Every deploy env should have an (different) instance.py file
# flake8: noqa
from .base import *
try:
    from .instance import *
except ImportError:
    pass
