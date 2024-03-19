"""
Abstract classes.

All of the abstract classes.
"""

import attrs

@attrs.define
class Timer:
    """A Timer object."""
    
    name: str
    """Name that is attached to the key."""
    key: str
    """The key attached to the timer."""
    end_time: int
    """The end time, in seconds, for when the timer will end."""
    has_ended: bool
    """Whether or not the timer has ended."""

