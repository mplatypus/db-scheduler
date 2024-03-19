"""
Exceptions.

All of the available exceptions within the db_scheduler library.
"""

from __future__ import annotations

import attrs

class DBSchedulerException(Exception):
    """The base database scheduler exception."""


class HandlerException(DBSchedulerException):
    """Raised when a handler fails to handle their exception."""


@attrs.define
class HandlerConnectException(HandlerException):
    """Raised when a handler cannot start."""

    reason: str
    """The reason for the connection failure."""
    