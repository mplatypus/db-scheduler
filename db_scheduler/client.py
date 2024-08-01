"""
Client.

The client for this database scheduler.
"""

from __future__ import annotations
import typing as t
import uuid
import asyncio

from .handlers import BaseHandler
from .abc import Timer

CallT = t.Callable[[Timer], t.Coroutine[t.Any, t.Any, None]]

class Client:
    """
    Client.
    
    The client, to control the connection, and database related functions.
    """

    def __init__(
        self,
        handler: BaseHandler,
    ) -> None:
        self._handler = handler

        self._listeners: list[tuple[str, t.Type[CallT]]]

        self._tasks: dict[str, asyncio.Task[None]] = {}

    async def start(self) -> None:
        """
        Start.

        Start up the clients connection to the database.
        """
        await self._handler.start()

        await self._handler.build_table()

    async def stop(self) -> None:
        """
        Stop.

        Stop the connection to the database.
        """
        await self._handler.stop()

    async def create(self, name: str, time: int) -> Timer:
        """
        Create timer.
        
        Create a new timer with the time specified.

        Parameters
        ----------
        time : int
            The time that the user sets, in seconds.
        """
        timer = Timer(name, str(uuid.uuid4()), time, False)

        await self._handler.add_timer(timer)

        # Start the timer.

        return timer


    async def delete(self, key: str) -> None:
        """
        Delete timer.

        Delete a timer, and stop it from ending.

        Parameters
        ----------
        key : str
            The key that the timer is attached too.
        """

    def listen(self, name: str):
        def listener(func: CallT):
            self._listeners.append((name, func))

        return listener