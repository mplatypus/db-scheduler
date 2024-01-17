import attrs
import enum

class TimerStatus(enum.Enum):
    """
    The current state, of the [Timer][dbtimer.abc.Timer]
    """
    FINISHED = 0
    """The timer has finished."""
    STARTED = 1
    """The timer has been started."""
    WAITING = 2
    """
    The timer is waiting to be started.
    
    !!! NOTE
        If its waiting, the time variable, will be -1.
    """


@attrs.define
class Timer:
    """
    Timer

    The base timer, that is returned when a Timer gets started, or ends.
    """
    name:str
    """The name, attached to a function, that it will call."""
    key: str
    """The key, or unique ID given."""
    time: int
    """The end time, of when this timer is to end. (-1 if the timer has not been started yet.)"""
    default_time: int
    """The default time, that this event will take."""
    status: TimerStatus
    """The current state of this timer."""
