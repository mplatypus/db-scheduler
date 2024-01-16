from __future__ import annotations

from .base import DatabaseBuilder
import typing as t

FuncT = t.Callable[[str], t.Coroutine[t.Any, t.Any, None]]

class Timer:
    def set_class(self, db: DatabaseBuilder) -> None:
        self._db_class = db

    async def create(self, delay: int, name: str) -> str:
        """
        Parameters
        ----------
        delay : int
            The delay in which it will take to trigger this timer.
        name : str
            The name of the function, that will run.
        """
        

        key = await self._db_class.create(name, delay)

        # Start the timer somewhere here.

        return key
    
    async def start(self) -> None:
        """
        Creates a loop, to check the status of the timers, and calls the events, when their time runs near.
        """

    def set_name(self, name: str) -> t.Callable[[FuncT], FuncT]:
  
  
        def decorator(func: FuncT) -> FuncT:
            return func
  
        return decorator
        