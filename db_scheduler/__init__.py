"""
DB Scheduler.

The database scheduler, for all your scheduling needs.
"""

from __future__ import annotations

from .about import __author__, __author_email__, __maintainer__, __license__, __url__, __version__
from .client import Client
from .handlers import BaseHandler, AIOSQLiteHandler
from .exceptions import DBSchedulerException, HandlerException, HandlerConnectException
from .abc import Timer

__all__ = (
    # .about
    "__author__", 
    "__author_email__", 
    "__maintainer__", 
    "__license__", 
    "__url__", 
    "__version__",
    # .abc
    "Timer",
    # .client
    "Client",
    # .exceptions
    "DBSchedulerException",
    "HandlerException",
    "HandlerConnectException",
    # .handler
    "BaseHandler",
    "AIOSQLiteHandler",
)