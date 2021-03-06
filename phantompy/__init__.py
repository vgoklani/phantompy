# -*- coding: utf-8 -*-

from .api import library as lib
from .api import ctypes

from . import page
from . import context
from . import image
from . import webelements


def open(url, size=(1280, 768), ctx=None):
    if ctx is None:
        ctx = context.get_context()

    p = page.Page(url=url, size=size, ctx=ctx)
    p.load()

    return p.frame()

