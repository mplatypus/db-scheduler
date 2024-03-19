"""
Handlers.

All the handlers for the library.
"""

import abc
import typing as t
import aiosqlite

from .exceptions import HandlerConnectException
from .abc import Timer

HandlerT = bool | str | int

class BaseHandler(abc.ABC):
    """
    Base Handler.

    All custom, and built in handlers must subclass this class.
    """

    @abc.abstractmethod
    async def start(self) -> None:
        """
        Start handler.
        
        The start up function, for the handler.
        """
        ...

    @abc.abstractmethod
    async def stop(self) -> None:
        """
        Stop handler.
        
        The stop, or shutdown function, for the handler.
        """
        ...

    @abc.abstractmethod
    async def build_table(self) -> None:
        """
        Build Table.

        Build the table for the database, or update it if it exists.

        !!! note
            Your table must include three items:
            
             - key (of type string)
             - end time (of type integer)
             - has ended (of type boolean)
        """
        ...

    @abc.abstractmethod
    async def add_timer(self, timer: Timer) -> None:
        """
        Add Table.

        Add a row to the database.

        Parameters
        ----------
        columns : dict[str, typing.Any]
            The column values (name, value)
        """
        ...
    
    @abc.abstractmethod
    async def fetch_timer(self, key: str) -> Timer | None:
        """
        Fetch Timer.

        Fetch a specific timer via its key.

        Parameters
        ----------
        key : str
            The key for the timer.

        Returns
        -------
        typing.Mapping[str, typing.Any]
            The information, from the timer (name, value)
        None
            No values were found.
        
        """
        ...
    
    @abc.abstractmethod
    async def fetch_all_timers(self) -> t.Sequence[Timer] | None:
        """
        Fetch All Timers.

        Fetch every single timer from the database.

        Returns
        -------
        typing.Sequence[typing.Mapping[str, typing.Any]]
            A list, of all timers (str: name, t.Any: value)
        None
            No value was found.
        """
        ...

    @abc.abstractmethod
    async def delete_timer(self, key: str | Timer) -> None:
        """
        Delete timer.

        Delete a specific timer.

        Parameters
        ----------
        key : str
             The key for the timer.
        """
        ...

    @abc.abstractmethod
    async def delete_all_timers(self) -> None:
        """
        Delete all timers.

        Delete all timers from the database.
        """


class AIOSQLiteHandler(BaseHandler):
    """
    AIOSQLite Handler.

    The SQLite handler.
    """

    def __init__(self, file_location: str) -> None:
        self._file_location: str = file_location

        self._connection: aiosqlite.Connection | None = None
        
        super().__init__()

    def _get_connection(self) -> aiosqlite.Connection:
        if isinstance(self._connection, aiosqlite.Connection):
            return self._connection
        
        raise HandlerConnectException("Not yet started.")

    async def start(self) -> None:
        self._connection = aiosqlite.connect(self._file_location)
        

    async def stop(self) -> None:
        if self._connection:
            await self._connection.close()
        

    async def build_table(self) -> None:
        conn = self._get_connection()

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS db_scheduler_store
            (
                key TEXT NOT NULL
                end_time BIGINT NOT NULL
                has_ended BOOLEAN NOT NULL
            );
            """
        )

        await conn.commit()
    
    async def add_timer(
        self,
        timer: Timer
    ) -> None:
        conn = self._get_connection()

        conn.execute(
            """
            INSERT INTO db_scheduler_store(key, end_time, has_ended)
            VALUES(?, ?, ?)
            """,
            (timer.key, timer.end_time, False)
        )

        await conn.commit()

    async def fetch_timer(self, key: str) -> Timer | None:
        conn = self._get_connection()

        cur = await conn.execute(
            """
            SELECT * FROM db_scheduler_store WHERE key = ?
            """,
            (key,)
        )

        value = await cur.fetchone()

        if value:
            return Timer(*value)

    async def fetch_all_timers(self) -> t.Sequence[Timer] | None:
        conn = self._get_connection()

        cur = await conn.execute(
            """
            SELECT * FROM db_scheduler_store
            """
        )

        values = await cur.fetchall()

        timer_list: t.MutableSequence[Timer] = []

        if values:
            for value in values:
                timer_list.append(Timer(*value))

            return timer_list
        
    async def delete_timer(self, key: str | Timer) -> None:
        conn = self._get_connection()

        conn.execute(
            """
            DELETE FROM db_scheduler_store WHERE key = ?
            """,
            (key,)
        )

        await conn.commit()

    async def delete_all_timers(self) -> None:
        conn = self._get_connection()

        conn.execute(
            """
            DELETE FROM db_scheduler_store
            """
        )

        await conn.commit()
