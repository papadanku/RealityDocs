
Debugging
=========

The BF2 engine has some debugging features, one of which is a log file that it can produce during the course of a game that records various pieces of information that would be useful in debugging. This BF2 engine log file can be written to from Python programs by using the ``host.log(msg)`` method. Unfortunately, no one seems to know how to turn this logging on right now–maybe it’s a command-line option? It’s even possible that the debugging features were stripped out of the retail version of the BF2 server, and so the log may be non-existent.

The core DICE Python code includes a Python debugging feature that sends it’s output to the BF2 engine log file via ``host.log``. It does this by redefining the stdout (standard output) and stderr (standard error message) I/O streams so that instead of going to the console (which is basically non-existent for the embedded Python interpreter), they are routed to ``host.log``, where they will be recorded along with any log information from the BF2 engine. Once this redefinition is done, a simple Python ``print`` statement will send its output to the log file.

The classes used to accomplish this output redirection are defined in ``bf2._init_``, but the actual redirection itself doesn’t happen until the BF2 engine calls the ``bf2.init_module()``\ … so any ``print`` statements executed before this will go nowhere.

In the ``bf2._init_`` module, close to the beginning of the file, is a line that says: ``g_debug = 0``. ``g_debug`` serves as a global flag that activates (=1) or deactivates (=0) the printing of debugging information throughout all BF2 Python modules. Throughout the DICE Python code, whenever the program has a bit of information that might be useful in debugging (often just a statement that “we reached this point”), the code checks the value of ``g_debug``, and if it’s 1, it prints the debugging information. (If you want to use g_debug as a switch for debugging information from your own modules, be sure to put ``from bf2 import g_debug`` in those modules).

So, why is this any good if ``host.log`` is a black hole? Because you can redirect redirect stdout and stderr yourself, to your own log file… inside ``bf2.init_module`` (in the file ``Battlefield 2 Server/python/_init_.py``, then look for the line that says “``def init_module():``”), look for the code that reads:

.. code-block:: python

   sys.stdout = fake_stream('stdout')
   sys.stderr = fake_stream('stderr')

and replace it with:

.. code-block:: python

   logFile = open('mylogfile.log', 'a')
   sys.stdout = logFile
   sys.stderr = logFile

(The ``'a'`` means that Python should “append” output to the end of the log file, as opposed to erasing it first). This change will cause anything every error message and the output of every ``print`` statement to be routed to the file ``Battlefield 2 Server/mylogfile.log``.

You can now use ``print`` statements in your own Python code as a way of getting feedback about what’s going on in your programming.

Important Consideration
-----------------------

Because of the way your operating system buffers I/O, you may not see anything in your log file until the ``stdout`` and ``stderr`` streams are closed or until the operating system’s internal buffer is full–which may not happen for quite a while… and maybe not until the server is shut down–and even then, your output may vanish completely if the server isn’t shutdown in an orderly way.

For example, if you are using the server GUI tool available from EA and you push the “Stop” button when the server is running, the server will shutdown abruptly without flushing it’s buffers–and you’ll find nothing in your log file. To shut the server down gracefully, type the “quit” command into the server’s window directly. If you’ve sent some particularly important information to the log file and you want to insure it gets there, you can use the ``sys.stdout.flush()`` method.

Note
----

You can use ``host.rcon_invoke('echo "..."')`` to print things directly to the server console.
