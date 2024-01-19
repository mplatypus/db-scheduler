# Libraries

This is a slowly updating list, of databases, supported by this library.

* [asyncpg](https://pypi.org/project/asyncpg/)

??? EXAMPLE "Class for asyncpg"

    ```python
    class Asyncpg(db_scheduler.DatabaseBuilder):
        _pool: t.Any | None = None

        @property
        def pool(self):
            if not self._pool:
                raise ValueError("You must connect the database for use.")
            return self._pool
        
        def __init__(
            self, 
            username: str, 
            password: str, 
            database: str,
            host: str = "127.0.0.1",
            port: int = 5432,
            **kwargs: t.Any
            ) -> None:
            self._kwargs: dict[str, t.Any] = {"user":username, "password":password, "database": database, "host":host, "port":port}

            self._kwargs.update(kwargs)

            print(self._kwargs)


        async def connect(self) -> None:
            self._pool = await asyncpg.create_pool(
                **self._kwargs, min_size=5, max_size=5
            )

        async def shutdown(self) -> None:
            await self.pool.close()

        async def _check_table(self) -> None:
            async with self.pool.acquire() as con:
                await con.execute("CREATE TABLE IF NOT EXISTS db_scheduler_store(name text NOT NULL, key text NOT NULL, time bigint NOT NULL, PRIMARY KEY (name, key))")

        async def add(self,timer: db_scheduler.Timer) -> None:
            await self._check_table()

            async with self.pool.acquire() as con:
                await con.execute("INSERT INTO db_scheduler_store(name, key, time) VALUES ($1, $2, $3)", timer.name, timer.key, timer.time)
        
        async def fetch(self, name: str, key: str) -> db_scheduler.Timer:
            await self._check_table()

            async with self.pool.acquire() as con:
                data = await con.fetchrow(  
                    "SELECT * FROM db_scheduler_store WHERE name = $1 AND key = $2", name, key
                )

            if data is None:
                raise ValueError("Timer not found.")

            return db_scheduler.Timer(*data.values())
        
        async def fetch_all(self) -> t.Sequence[db_scheduler.Timer] | None:
            await self._check_table()

            async with self.pool.acquire() as con:
                data = await con.fetch(  
                    "SELECT * FROM db_scheduler_store"
                )

            if len(data) <= 0:
                return
            
            timer_list: list[db_scheduler.Timer] = []
            for record in data:
                timer_list.append(db_scheduler.Timer(*record.values()))

            return timer_list

        async def delete(self, name: str, key: str) -> None:
            await self._check_table()

            async with self.pool.acquire() as con:
                await con.execute("DELETE FROM db_scheduler_store WHERE name = $1 AND key = $2", name, key)
        
        async def delete_all(self, name: str) -> None:
            await self._check_table()

            async with self.pool.acquire() as con:
                await con.execute("DELETE FROM db_scheduler_store WHERE name = $1", name)

        async def clear(self) -> None:
            await self._check_table()

            async with self.pool.acquire() as con:
                await con.execute("DELETE FROM db_scheduler_store")
    ```

* [Aiosqlite](https://pypi.org/project/aiosqlite/)

??? EXAMPLE "Class for aiosqlite"

    ```python
    class AioSqlite(db_scheduler.DatabaseBuilder):
        _connection: aiosqlite.Connection | None = None

        def __init__(self, file_location: str) -> None:
            self._file_location = file_location

        @property
        def connection(self) -> aiosqlite.Connection:
            if not self._connection:
                raise ValueError("Database must be initialized before use.")

            return self._connection

        async def connect(self) -> None:
            self._connection = await aiosqlite.connect(self._file_location)

        async def shutdown(self) -> None:
            await self.connection.close()

        async def _check_table(self) -> None:
            async with self.connection.cursor() as con:
                await con.execute("CREATE TABLE IF NOT EXISTS db_scheduler_store (name TEXT NOT NULL, key TEXT NOT NULL, time INTEGER NOT NULL, default_time INTEGER NOT NULL, status INTEGER NOT NULL, PRIMARY KEY(name, key))")
            
            await self.connection.commit()

        async def add(self,timer: db_scheduler.Timer) -> None:
            await self._check_table()

            async with self.connection.cursor() as con:
                await con.execute("INSERT INTO db_scheduler_store(name, key, time, default_time, status) VALUES (?, ?, ?, ?, ?)", (timer.name, timer.key, timer.time, timer.default_time, timer.status.value))

                await self.connection.commit()
        
        async def fetch(self, name: str, key: str) -> db_scheduler.Timer:
            await self._check_table()

            async with self.connection.cursor() as con:
                await con.execute(  
                    "SELECT * FROM db_scheduler_store WHERE name = ? AND key = ?", (name, key)
                )
                await self.connection.commit()

                data = await con.fetchone()

            if data is None:
                raise ValueError("Timer not found.")

            return db_scheduler.Timer(*data)
        
        async def fetch_all(self) -> t.Sequence[db_scheduler.Timer]:
            await self._check_table()

            async with self.connection.cursor() as con:
                await con.execute(  
                    "SELECT * FROM db_scheduler_store"
                )
                await self.connection.commit()

                data = await con.fetchall()
            
            timer_list: list[db_scheduler.Timer] = []
            for record in data:
                timer_list.append(db_scheduler.Timer(*record))

            return timer_list

        async def delete(self, name: str, key: str) -> None:
            await self._check_table()

            async with self.connection.cursor() as con:
                await con.execute("DELETE FROM db_scheduler_store WHERE name = ? AND key = ?", (name, key))

                await self.connection.commit()
        
        async def delete_all(self, name: str) -> None:
            await self._check_table()

            async with self.connection.cursor() as con:
                await con.execute("DELETE FROM db_scheduler_store WHERE name = ?", name)

                await self.connection.commit()

        async def clear(self) -> None:
            await self._check_table()

            async with self.connection.cursor() as con:
                await con.execute("DELETE FROM db_scheduler_store")

                await self.connection.commit()

    ```