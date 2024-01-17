# Basics

Here is an example of the full code:
```python
import dbtimer
import asyncio

from somewhere import AioSqlite

timer_db = AioSqlite("testing.db")

timer = dbtimer.TimerClient(timer_db)

time = int(input("enter a time (seconds)? "))

async def main():
    await timer.load()

    new_timer = await timer.create(time, "test")

    await timer.start(new_timer)

    print("timer key:", new_timer.key)

    while True:
        await asyncio.sleep(1)

@timer.listen("test")
async def test_listener(time: dbtimer.Timer):
    print(f"Timer finished successfully! Key: {time.key}")

    await timer.unload()

asyncio.run(main())
```

Now, this is a bit of a mouthful, so lets break it apart:

```python
import asyncio
import dbtimer
```

These are the basic python imports. The library [asyncio](https://docs.python.org/3/library/asyncio.html) and this library.

```python
from somewhere import AioSqlite
```

This, is an import of a [custom database](../getting_started/custom_database.md). More about this, will be explained later.

```python
timer_db = AioSqlite("testing.db")
```

This is the setup of the database class. All databases will be different. This is the most basic option, in terms of database options.
All you have to do, is pass the file as a build argument (in this case, its `testing.db`)

```python
timer = dbtimer.TimerClient(timer_db)
```

Your timer client. This is the object, that you can create, start and cancel timers from, and also add timer functions.

```python
time = int(input("enter a time (seconds)? "))
```

This is a simple input to allow for the user to set and test different times.

```python
async def main():
```

This is to allow, for the main, asynchronous function.

```python
await timer.load()
```

This loads the timer. it does 3 main functions internally.

* Starts up the database
* Checks and starts tasks for other timers
* Starts a general task, to keep checking the timers

Without any of these three functions, this bot simply wont do anything. You **MUST** always include the `load()` function somewhere in your code.

```python
new_timer = await timer.create(time, "test")
```

This function, creates you a new timer, by taking two arguments.

Argument 1: An integer, for the amount of time you wish to wait. This is supposed to be an amount of time into the future.

??? note "About Argument 1"
    For argument 1, you want to feed the time in seconds, from the current time. So for example if the current time is 3:00pm, and you want a timer to go off for 4:00pm, then you want to parse 3600.

Argument 2: A string, that has been set for a custom listener (explained later.)

```python
await timer.start(new_timer)
```

This function, will start the timer, you have created, from the time it has started.

```python
print("timer key:", new_timer.key)
```

This is simply to show you, what the key is. [what is a key for?](../getting_started/index.md#what-is-a-key-and-what-is-it-for)

```python
while True:
    await asyncio.sleep(1)
```

This is also, just to keep the program alive. It is not required, and is only used for the example, otherwise, the program ends before you can fully use it.d

```python
@timer.listen("test")
```

This is the function, that will allow for you to "listen" for that keyword, in the database. The below function, must be attached, for this to work.

```python
async def test_listener(time: dbtimer.Timer):
```

This function, has an argument of the timer, and where you can see, that exact key that was created when you ran `timer.create()`

```python
print(f"Timer finished successfully! Key: {time.key}")
```

This prints the key, and lets you know that the timer finished successfully.

```python
await timer.unload()
```

This, unloads (disconnects the database) in a safe, and controlled manor.

```python
asyncio.run(main())
```

And lastly, this just simply runs the asynchronous code!