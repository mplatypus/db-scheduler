from __future__ import annotations

import abc
import attrs
import typing as t

@attrs.define
class TimerObj(abc.ABC):
    name: str
    key: str
    time: int

class DatabaseBuilder(abc.ABC):
    """
    Create a new timer.

    All timers must be created, 
    """
    @abc.abstractmethod
    async def create(self, name: str, time: int) -> str:
        """create a new timer. Must return a unique ID."""
        ...
    
    @abc.abstractmethod
    async def fetch(self, name: str, key: str) -> TimerObj:
        """fetch a timers time."""
        ...

    @abc.abstractmethod
    async def fetch_all(self) -> t.Sequence[TimerObj]:
        """fetch all timers times."""
        ...

    @abc.abstractmethod
    async def delete(self, name: str, key: str) -> None:
        """Delete a specific timer."""
        ...

    @abc.abstractmethod
    async def delete_all(self, name: str) -> None:
        """Delete all timers of that name."""
        ...

    @abc.abstractmethod
    async def clear(self) -> None:
        """Clear all timers."""
        ...

    
    
