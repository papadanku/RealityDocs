
Time in BF2
===========

Time is principly measured within Battlefield 2 by means of “wall time”–the time in high-resolution seconds since the server started running (e.g. ``443.451488108``). Note that since the BF2 server does not restart between rounds (unlike the servers for *Battlefield: 1942* and *Battlefield: Vietnam*, which both practially reboot between rounds), wall time continues to increase from round to round.

.. code-block:: python
   :caption: The current wall time can be determined this way

      timeNow = host.timer_getWallTime()

Most *(all?)* time-related measurements inside BF2 are in seconds, and are based on wall time.

.. code-block:: python
   :caption: Other time functions are also available

      import time

      # Gives current epoch time (seconds since 1970 Jan 1)
      epochTime = time.time()
      # Or, to get a formatted string containing a more user-friendly date and time
      dateString = time.strftime("%m-%d-%y %H:%M")

See the `Python Library Reference <https://docs.python.org/release/2.3.4/lib/module-time.html>`__ for more information about ways to manipulate dates and times in Python.
