# Getting Started

This is where you can come to, for all your information, on creating your own database timer!

## Q's and A's

### What is a key, and what is it for?

A key, is not something that is needed to be used, but can be used.

For your functions around the controlling of the database, you may want to be able to store extra data, say, an ID, or a name, or a colour even.
For this, adding custom meta-data could have been done, but was chosen not to, due to complexity, and bad practices, and the code also not being safe.

So now you might be wondering, how a key can help.

It's really simple!

when you call the following:
```python
TimerClient.create()
```

it will create you a new timer object.

This timer object, will include a custom "key" attached to that timer, that will be unique from every other timer you have.

Then, with that key, you can have a separate database table, with a parameter for said key. 
then, when that function comes up again, all you simply have to do, call that table, with the key, and you can get your specialized data.